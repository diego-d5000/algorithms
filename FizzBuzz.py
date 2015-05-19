# in a range from 1 to 100 print Fizz if the number is multiplie of 3 
#and Buzz of 5, if both print FizzBuzz

def fizzBuzz():
	for i in range(1,100):
		if i % 3 is 0 and i % 5 is 0:
			print("FizzBuzz")
		elif i % 3 is 0:
			print("Fizz")
		elif i % 5 is 0:
			print("Buzz")
		else:
			print(i)