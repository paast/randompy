import json
import random



def chain(network):
	chain = []
	chain += ['<start>']
	while (chain[-1] != "<end>"):
		current = chain[-1]
		r = random.random()
		hold = 0
		for k, v in network[current].items():
			hold += network[current][k]
			if (hold >= r):
				chain += [k]
				break


	return chain

def refine(sentence):

	t = ""

	punct = ['.', ',', '?', '!', '-']
	for i, token in enumerate(sentence):
		if (token in punct and sentence[i - 1] == " "):
			t = t[:-1]
		t += token

	return t

def main():

	data = json.loads(open("C6928G0MA-net.json", "r").readline())

	print('')
	for n in range(5):
		temp = ' '.join(chain(data))
		temp = refine(temp)
		print(temp, '\n')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__": main()