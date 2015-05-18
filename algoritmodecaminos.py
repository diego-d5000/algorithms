ways = []

def nextV(v,A):
	ways = []
	for a in A:
		if a.find(v) is 1:
			ways.append(a[0])
		elif a.find(v) is 0:
			ways.append(a[1])
	return ways

def graphWay(i,f,A):
	#i=a f=h A= [ab,ad,bf,bg,gh]
	global ways
	way = [i]   # way = [a]
	nextAs = nextV(i,A) # nextAs = [b,d]
	for a in nextAs:
		way.append(a) # way = [a,b]
		if a is f:
			ways.append(way)
			break
		else:
			nextAs = nextV(a,A)




A = ["ab","ac","da","db","fc"]
v = "a"

print nextV(v,A)

raw_input()

