import requests
import time


VERBOSE = False


def furl(title):
	"""Returns full forward-link url based on title input"""

	# url to forward links json
	furl = ('https://en.wikipedia.org/w/api.php?' +
			'action=query&prop=links&titles={PAGE}' +
			'&plnamespace=0&pllimit=max&format=json' +
			'&formatversion=2')

	return furl.format(PAGE=title)

def burl(title):
	"""Returns full backward-link url based on title input"""

	# url to backward links json
	burl = ('https://en.wikipedia.org/w/api.php?' +
			'action=query&prop=linkshere&titles={PAGE}' +
			'&lhnamespace=0&lhlimit=max&format=json' +
			'&lhprop=title&formatversion=2')

	return burl.format(PAGE=title)

def load_forward(src_node, url):
	"""Gets url, converts response to JSON,
	parses JSON to produce a list of links.
	(for use in pl-type queries)"""

	r_set = set({})
	temp = requests.get(url).json()

	if 'continue' in temp:
		cont_param = '&plcontinue=' + temp['continue']['plcontinue']
		r_set |= load_forward(src_node, url + cont_param)
	
	if 'links' in temp['query']['pages'][0]:
		for link in temp['query']['pages'][0]['links']:
			r_set.add(Node(src_node, link['title']))

	return r_set

def load_backward(src_node, url):
	"""Gets url, converts response to JSON,
	parses JSON to produce a list of links.
	(for use in lh-type queries)"""

	r_set = set({})
	temp = requests.get(url).json()

	if 'continue' in temp:
		cont_param = '&lhcontinue=' + temp['continue']['lhcontinue']
		r_set |= load_backward(src_node, url + cont_param)
	if 'linkshere' in temp['query']['pages'][0]:
		for link in temp['query']['pages'][0]['linkshere']:
			r_set.add(Node(src_node, link['title']))

	return r_set


class Node:
	"""A node which has a source node.
	If root, src = None"""
	name = None

	def __init__(self, src, name):
		self.src = src
		self.name = name
		self.expanded = False

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __hash__(self):
		return hash(self.name)

	def print_trail(self):
		hold = []
		if self.src is not None:
			hold += self.src.print_trail()
		hold += [self.name]
		return hold


def find_path(start, end):

	f_set = {Node(None, start)}
	b_set = {Node(None, end)}

	# control flow variable
	route = 1

	# 0 = match, 1 = forward, -1 = backward
	while route != 0:
		test = f_set.intersection(b_set)

		if (f_set.intersection(b_set)):
			route = 0

		temp = set({})

		if route == 0: break
		elif route == 1:
			for i, node in enumerate(f_set):
				if node.expanded == False:
					temp |= load_forward(node, furl(node.name))
					if (VERBOSE): print(i, "/", len(temp))
					node.expanded = True
					if b_set.intersection(temp):
						route = 0
						break
			f_set |= temp
			route = -1
		elif route == -1:
			for i, node in enumerate(b_set):
				if node.expanded == False:
					if (VERBOSE): print(i, "\\", len(temp))
					temp |= load_backward(node, burl(node.name))
					node.expanded = True
					if f_set.intersection(temp):
						route = 0
						break
			b_set |= temp
			route = 1
		else:
			# sanity check
			raise ValueError("Unreasonable control flow value: ", route)

	test1 = [x for x in f_set if x in b_set]
	test2 = [x for x in b_set if x in f_set]

	test1 = test1[0].print_trail()
	test2 = test2[0].print_trail()
	del test2[-1]

	test3 = test1 + test2[::-1]

	return(test3, len(f_set) + len(b_set))


def main():
	input = ("LaunchCode", "Alison_Richard")

	start = time.time()
	r, l = find_path(input[0], input[1])
	end = time.time()

	elapsed_time = end - start

	print("START:", input[0])
	print("END:", input[1])
	print("NODES:", l)
	print("DEGREE:", len(r) - 1)
	print("PATH:", ' -> '.join(r))
	print("TIME:", elapsed_time) 




#~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__": main()
