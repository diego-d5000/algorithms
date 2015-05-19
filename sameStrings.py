#Given 2 arrays of string, print an array of strings common in the two arrays

def sameStrings(arg1, arg2):
	sameStrs = []
	for i in arg1:
		for k in arg2:
			if k == i:
				sameStrs.append(k)
	print sameStrs