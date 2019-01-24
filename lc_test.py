#list concatenation test



def recursive_concat(n):
	hold = []
	if (n > 0):
		hold += recursive_concat(n-1)
	hold += [n]
	return hold

print(recursive_concat(7))