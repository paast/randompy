
# Grid size
# Random start point
# Controlled probability
# Generate as needed to detect continuation or not
# Quick-finish to get final density

import random

grid_size = 10


class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def val(self):
		return (self.y  * 10 + self.x)

	def __repr__(self):
		return ("<" + str(self.x) + "," + str(self.y) + ">")

	def __eq__(self, other):
		return (self.val() == other.val())

	def __hash__(self):
		return hash(self.val())



def run():
	print(sim(0.5, 1))


def sim(p, n):
	times = []
	for i in range(n):
		matrix = [[(0 if random.random() < p else 1) for x in range(grid_size)] for y in range(grid_size)]
		start = Point(random.randrange(grid_size), random.randrange(grid_size))
		times.append(fire(matrix, start))
	return times

def fire(m, start):
	t = 0
	edge = set({start})
	while (len(edge) > 0 and t < 20):
		pM(m)
		a_hold = r_hold = set({})
		for point in edge:
			adjs = getAdj(point.getX(), point.getY(), grid_size)
			for adj in adjs:
				x = adj.getX()
				y = adj.getY()
				if (m[y][x] == 1):
					m[y][x] == 0
					a_hold.add(adj)
			r_hold.add(point)
		edge -= r_hold
		edge |= a_hold
		t += 1
		print(t)

	return t

def getAdj(x, y, s):
	adj = []
	for i in range (-1, 2):
		for j in range (-1, 2):
			dx = x + j
			dy = y + i
			if ((dx != x or dy != y) and (-1 < dx < s and -1 < dy < s)):
				adj.append(Point(dx, dy))
	return adj

def pM(m):
	for y in m:
		for x in y:
			if (x == 0):
				print(". ", end='')
			else:	
				print("8 ", end='')
		print()



# ~~~~~~~~~~~~~~~

if __name__ == "__main__":
	run()



