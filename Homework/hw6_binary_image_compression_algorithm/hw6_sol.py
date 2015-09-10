'''
Created on Mar 09, 2015
@author:   Kelvin Rodriguez
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# I made a separate function for each step of the process for legibility
# tried being short and concise.

# first define all helper functions for compress()
# helper function for splice()
def count(S):
	'''returns the total number of consecutive characters.'''
	if len(S) == 1 : return 1
	elif S[0] == S[1] : return 1 + count(S[1:])
	return 1

def splice(S):
	'''returns a list of numbers each representing the number of consecutive
	characters in a string S.'''
	if S == '' : return []
	return [count(S)] + splice(S[count(S):])

# helper function for numToBinary()
def isOdd(n):
	'''returns whether or not n is an odd integer.'''
	if n % 2 == 0 : return False
	return True

def numToBinary(n):
	'''returns the binary representation the number n.'''
	if n == 0 : return ''
	elif isOdd(n) : return numToBinary(n // 2) + '1'
	return numToBinary(n // 2) + '0'

def breakup(n):
	'''returns a representation of n that can be converted to
	binary for COMPRESSED_BLOCK_SIZE bits.'''
	if n <= MAX_RUN_LENGTH : return [n]
	return [MAX_RUN_LENGTH, 0] + breakup(n - (MAX_RUN_LENGTH))

def collapse(lst):
	'''returns a list of all the elements within lst.'''
	if lst == [] : return lst
	elif isinstance(lst[0], list) : return collapse(lst[0]) + collapse(lst[1:])
	return [lst[0]] + collapse(lst[1:])

def combine(lst):
	'''returns a list of all the elements in lst concatenated.'''
	if lst == [] : return ''
	return lst[0] + combine(lst[1:])

def compress(S):
	'''returns a binary string via run-length encoding of the
	input string.'''
	# binary representation of the elements in S after counting
	# consecutive 0s and 1s
	A =  map(numToBinary,collapse(map(breakup, splice(S))))
	# padding of A's elements for COMPRESSED_BLOCK_SIZE bits
	B =  map(lambda S : (COMPRESSED_BLOCK_SIZE - len(S)) * '0' + S, A)
	if S[0] == '0' : 
		return combine(B)
	return COMPRESSED_BLOCK_SIZE * '0' + combine(B)

# helper functions for uncompress()
def split(S):
	'''returns a list of strings with the S broken up into segments
	equal to COMPRESSED_BLOCK_SIZE.'''
	if S == '' : return []
	return [S[0:COMPRESSED_BLOCK_SIZE]] + split(S[COMPRESSED_BLOCK_SIZE:])

def binaryToNum(S):
	'''returns the integer corresponding to the binary representation in
	s. Note: the empty string represents 0.'''
	if S == '' : return 0
	return int(S[-1]) + 2 * binaryToNum(S[:-1])

def uncompress_helper(L):
	'''returns a string of consecutive 0s and 1s based off L[0] for 0s and L[1] for
	1s. This is a helper function for uncompress.'''
	if len(L) == 1 : return L[0] * '0'
	elif len(L) == 2 : return L[0] * '0' + L[1] * '1'
  	return L[0]*'0' + L[1]*'1' + uncompress_helper(L[2:])

def uncompress(C):
	'''returns a string of 0s and 1s by inverting the compression done 
	by compress() i.e. uncompress(compress(S)) returns S.'''
	if C == '' : return ''
	return uncompress_helper(map(binaryToNum, split(C)))

def compression(S):
	'''returns the ratio of the compressed size to the original size for
	the image S.'''
	return float(len(compress(S))) / float(len(S))

# The largest number of bits that the compress algorithm could possibly use
# to encode a 64-bit string/image is COMPRESSED_BLOCK_SIZE * 64, and with the 
# convention an additional 5 bits are needed. Tests were performed on the "Five" 
# and "Smile" images in the lab writeup (see test_hw6.py). The compression 
# ratios were 1.015625 and 1.328125 respectively. 

# Professor Lai is Lai-ing and such an algorithm cannot exist because there are 
# certain instances in which you would need more than 64-bits to represent a 64-bit 
# string. A perfect example would be the string '01' * 32, which is a string of
# alternating 0s and 1s. This string would require 320 bits to be represented with 
# a 5 bit compress algorithm. Another perfect example would be the string '10' * 32,
# which would require an additional 5 bits due to the convention or 325 bits. 
# Point in case, Prof Lai is lying. 

# END