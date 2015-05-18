def BubbleSortSwaps(arg):
	swaps = 0
	for n in range(len(arg)-1) :
		if arg[n] > arg[n+1] :
			swaps += 1
			temp = arg[n]
			arg[n] = arg[n+1]
			arg[n+1] = temporal
	return swaps


array = [34, 80, 6, 1, 1, 0, 89]

print array

print BubbleSortSwaps(array)

raw_input()