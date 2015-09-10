'''
Created on Feb 27, 2015
@author: Kelvin Rodriguez
'''
import turtle

def svTree(trunkLength, levels):
    '''Creates a recursive image of a tree made of line segments. Input
    trunkLength corresponds to the initial trunk length, and levels
    corresponds to the number of branches in the tree.'''
    if levels == 0 : 
        return
    else:
        turtle.forward(trunkLength)
        turtle.left(30)
        svTree(trunkLength / 2, levels - 1)
        turtle.right(60)
        svTree(trunkLength / 2, levels - 1)
        turtle.left(30)
        turtle.penup()
        turtle.backward(trunkLength)
        turtle.pendown()

def fastFib(n):
    '''Returns the nth Fibonacci number using the memoization technique
    shown in class and lab. Assume that the 0th Fibonacci number is 0, so
    fastFib(0) = 0, fastFib(1) = 1, and fastFib(2) = 1'''
    def fastFibHelper(n, memo):
    	'''helper function for fastFib using the memoization technique'''
    	if (n) in memo : return memo[(n)]
    	if n <= 1 : result = n
    	else:
    		result = fastFibHelper(n - 1, memo) + fastFibHelper(n - 2, memo)
    		memo[(n)] = result
    	return result
    return fastFibHelper(n, {})

# END