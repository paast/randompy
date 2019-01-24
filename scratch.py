# scratch pad

N = 100

for n in range(1, N):
	print(n, '-> ', end='')
	while (n % 4 != 3):
		if n % 2 == 0:
			n = int(n * (3 / 2))
		else:
			n = int((n - 1) * (3 / 4) + 1)
		if (n == 1):
			n = -1
	print(int((n + 1) / 4))