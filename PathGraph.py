#incomplete

ways = []

def waysNode(v,A):
	ways = []
	for a in A:
		if a.find(v) is 1:
			ways.append(a[0])
		elif a.find(v) is 0:
			ways.append(a[1])
	return ways

def findFinish(a,f,A):
	global ways
	way = [a]
	nextAs = waysNode(a,A)
	for a in nextAs:
		way.append(a)
		if a is f:
			ways.append(way)
			break
		else:
			nextAs = waysNode(a,A).remove(len(way)-1)




A = ["ab","ac","da","db","fc"]
v = "a"

print waysNode(v,A)

raw_input()

