'''
Created on Feb 23, 2015
@author: Kelvin Rodriguez
'''

# helper function for pascal_row()
def helper(L):
	'''returns a list of sums of adjacent elements within list L'''
	if len(L) == 1 : return []
	return [L[0] + L[1]] + helper(L[1:])

def pascal_row(n):
	'''returns a list of elements found in a certain row of
	Pascal's Triangle (i.e. the nth row).'''
	if n == 0 : return [1]
	elif n == 1 : return [1, 1]
	return [1] + helper(pascal_row(n - 1)) + [1]

def pascal_triangle(n):
	'''returns a list of lists containing the values of all the
	rows for Pascal's triangle up to and including row n.'''
	if n == 0 : return [[1]]
	return pascal_triangle(n - 1) + [pascal_row(n)]

# END