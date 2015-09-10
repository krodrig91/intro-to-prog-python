'''
Created on Feb 04, 2015
@author: Kelvin Rodriguez
'''

def mult(x, y):
	'''returns the product of x and y'''
	return x * y

def factorial(n):
	'''takes a positive integer, n, and returns n!'''
	if n == 0:
		return 1
	return reduce(mult, range(1, n + 1))
	
def mean(L):
	'''returns mean of input list L as a floating point'''
	return reduce(lambda x, y : x + y, L) / float(len(L))

def div(k):
	'''returns whether or not the remainder of 42 / k is = 0'''
	return 42 % k == 0

def divides(n):
	'''returns a function to determine if other numbers divide n''' 
	def div(k):
		'''uses int k and returns true if n is divisible by k'''
		return n % k == 0
	return div

def prime(n):
	'''returns whether or not n is a prime number'''
	if (n > 2):
		return not(reduce(lambda x, y : x or y, map(divides(n), range(2, n))))
	return n == 2

# END