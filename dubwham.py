import requests
import time











def find_path(start, end):

	f_set = Xset(Node(None, start))
	b_set = Xset(Node(None, end))

	iter_size = 250
	path = False

	while (path == False):
		# find which one to expand
		# and calculate expansion amount




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Node:
	"""A node which has a source node.
	If root, src = None"""

	def __init__(self, src, name):
		self.src = src
		self.name = name

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

class Xset:

	def __init__(self, origin_node):
		self.origin = origin_node
		self.x_set = set({})
		self.unx_set = set({origin_node})
		self.step = 0
		self.current_node = None
		self.continue_param = None

	def expand_forward(self, n):
		lc = 0
		while (lc < n):
			# do expansion and add node count
			# to lc

	def expand_backward():

	def intersect(self, other):
		# find minimal-work intersection


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
	temp = ("LaunchCode", "Alison_Richard")

	find_path(temp[0], temp[1])



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__": main()