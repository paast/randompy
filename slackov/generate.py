import json
import re

def purify(message):
	"""Replaces certain occurances
	from the message in question with
	more token-friendly phrases:

	- Links -> "<link>"
	- User-references -> "<user>"
	- Emojis -> "<emoji>" """

	links = re.findall(r"<http\S+>", message)
	users = re.findall(r"<@U\S+>", message)
	emojis = re.findall(r":.+:", message)

	for link in links:
		message = message.replace(link, "<link>")
	for user in users:
		message = message.replace(user, "<user>")
	for emoji in emojis:
		message = message.replace(emoji, " <emoji> ")
	return message

def split(message):
	"""Splits the message into tokens,
	removes certain tokens, and returns
	the tokens as a list."""
	
	ignore = ["\n", "(", ")", "*", "_", "", " "]

	split = re.split(r"""([ !?.,:&\-\n"*_()])""", message)

	return(['<start>'] + [x for x in split if x not in ignore] + ['<end>'])

def build_network(tokenized_msgs):
	"""Creates a Markov network represented
	by a dictionary of dictionaries. Where
	the top-level dicts are token-keys keying
	the inner dicts that contain weighted branches."""
	
	net = {}

	# create network
	for msg in tokenized_msgs:
		for i, token in enumerate(msg):
			if (token == "<end>"):
				break
			if token not in net:
				net[token] = {}
			nxt = msg[i+1]
			if nxt not in net[token]:
				net[token][nxt] = 0
			net[token][nxt] += 1

	# # remove singletons
	# for dic in net.values():
	# 	hold = []
	# 	for k, n in dic.items():
	# 		if (n == 1 != "<end>"):
	# 			hold += [k]
	# 	for key in hold:
	# 		del dic[key]

	# normalize weights
	for dict_o in net.values():
		total = 0
		for count in iter(dict_o.values()):
			total += count
		for k, w in dict_o.items():
			dict_o[k] = int((w / total) * 100000) / 100000

	return net


def main():

	messages = json.loads(open("C6928G0MA-dump.json", "r").readline())

	test_data = messages[:10]

	tokened = []
	
	for msg in messages:
		msg = purify(msg)
		tokened += [split(msg)]

	network = build_network(tokened)

	print(network['stack'])



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__": main()