
def get_initials(name):
	name = name.lstrip().rstrip().upper()
	inits = ''
	prev_char = None
	for char in name:
		if prev_char == None or prev_char == ' ':
			inits += char
		prev_char = char
	return(inits)

def new(name):
	name = name.lstrip().rstrip().split(' ')
	return ''.join([i[0].upper() for i in name])

def main():
	print(get_initials(str(input("Give full name:\n"))))
	print(new(str(input('Give full name:\n'))))

if __name__ == "__main__": main()
