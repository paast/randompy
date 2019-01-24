# prints out main NUE sets

def main():
	N = 100

	n_set = [''] * N
	for n in range(N):
		if (n % 2 != 0):
			x = (n // 2) * 3 + 2
			n_set[n] = 'n(' + str(x) + ')'
		else:
			if (n % 4 == 0):
				x = (n // 4) * 3
				n_set[n] = 'e(' + str(x) + ')'
			elif(n % 4 == 2):
				x = (n // 4) * 3 + 2
				n_set[n] = 'u(' + str(x) + ')'

	u_set = [''] * N
	for n in range(N):
		if (n % 2 != 0):
			x = (n // 2) * 3 + 1
			u_set[n] = 'n(' + str(x) + ')'
		else:
			if (n % 4 == 0):
				x = (n // 4) * 3
				u_set[n] = 'u(' + str(x) + ')'
			elif(n % 4 == 2):
				x = (n // 4) * 3 + 1
				u_set[n] = 'e(' + str(x) + ')'

	e_set = [''] * N
	for n in range(N):
		if (n % 2 != 0):
			x = (n // 2)
			e_set[n] = 'n(' + str(x) + ')'
		else:
			if (n % 4 == 0):
				x = (n // 4)
				e_set[n] = 'u(' + str(x) + ')'
			elif(n % 4 == 2):
				x = (n // 4)
				e_set[n] = 'e(' + str(x) + ')'

	for i in range(N):
		print("n(", i, ") -> ", n_set[i], '\t\t',
			  "u(", i, ") -> ", u_set[i], '\t\t',
			  "e(", i, ") -> ", e_set[i], sep='')

if (__name__ == "__main__"): main()
