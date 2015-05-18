def nmax(arg):
	max = arg[0]
	for n in arg:
		if n > max:
			max = n
	return max

array = [34, 80, 6, 66, 8, 7, 97, 63, 3, 27, 1, 1, 89]

print array

print nmax(array)

raw_input()