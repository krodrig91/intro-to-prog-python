'''
Created on Mar 30, 2015
@author: Kelvin Rodriguez
'''

# TcToNum() helper function
def binaryToNum(s): 
	'''returns the integer corresponding to the binary representation in s.
	precondition: s is a string of 0s and 1s.'''
	if s == '' : return 0
	return int(s[-1]) + 2 * binaryToNum(s[:-1])

def TcToNum(s):
	'''returns the corresponding integer representation of the input string s.
	precondition: s is always 8 bits.'''
	if s[0] == '0' : return binaryToNum(s)
	else : return binaryToNum(s) - 256

# NumToTc() helper function
def pad(s):
	'''returns a padded string s with leading zeros if len(s) < 8.'''
	if len(s) == 8 : return s
	return pad('0' + s) 

# NumToTc() helper function
def numToBinary(n):
	'''returns the string with the binary representation of non-negative integer n.
	precondition: integer argumetn is non-negative.'''
	if n == 0 : return ''
	return numToBinary(n / 2) + str(n % 2)

def NumToTc(n):
	'''returns a string representing the two's-complement representation of
	that integer.'''
	if n > 127 or n < -128 : return 'Error'
	elif n >= 0 : return pad(numToBinary(n))
	return pad(numToBinary(n + 256))

# END