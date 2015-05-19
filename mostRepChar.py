#func receive and string and print the most repeated char in that 
#and number of repeat

def mostRepChar(arg):
	nletter = 0
	letter = ""
	for i in arg:
		if arg.count(i) > nletter:
			nletter =  arg.count(i)
			letter = i
	print "the char most popular in your string is" 
	print letter
	print "appears: "
	print nletter