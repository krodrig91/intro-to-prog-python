'''
Created on Feb 10, 2015
@author: Kelvin Rodriguez
'''

import sys
sys.setrecursionlimit(10000)	# set recursion limit

# points associated with each letter
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

# dictionary used for testing 
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# define preliminary functions

def letterScore(letter, scorelist):
	'''returns the score associated with letter in scorelist'''
	if letter == '':
		return "You didn't enter a letter." # ignores other data types
	elif letter == scorelist[0][0]:
		return scorelist[0][1]
	return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
	'''returns the score associated with string S based off scorelist'''
	if S == '':
		return 0
	return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

# define 3 helper functions for scoreList()

def myFilter(Rack):
	'''returns a new list that contains all elements of Dictionary for
	which the predicate returns True i.e. words that Rack can make'''
	if Rack == []:
		return Rack
	return filter(lambda word : makeWord(word, Rack), Dictionary)

def makeWord(word, Rack):
	'''returns whether or not an input word can be made from the input Rack'''
	if word == '':
		return True
	elif Rack == []:
		return False
	elif word[0] in Rack:
		return makeWord(word[1:], removeLetter(word[0], Rack))
	return False

def removeLetter(letter, Rack):
	'''returns a list with a used letter removed from the Rack'''
	if Rack == []:
		return Rack
	elif Rack[0] == letter:
		return Rack[1:]
	return [Rack[0]] + removeLetter(letter, Rack[1:])

# scoreList() and bestWord() utilize 3 helper functions defined above

def scoreList(Rack):
	'''returns a list of all the words in the global Dictionary that can
	be made from the letters in the list of letters Rack'''
	if Rack == []:
		return Rack
	return map(lambda word : [word, wordScore(word, scrabbleScores)], myFilter(Rack))

# define helper function for bestWord() to find max valued word
# there's probably a fancier way of doing this but it works
def maxWord(lst):
	'''returns the maximum valued word found with the given Rack in bestWord(), 
	the input list contains all possible words with given Rack'''
	if lst == []:
		return ['', 0]
	elif lst[1:] == []:
		return [lst[0][0], lst[0][1]]
	elif lst[0][1] > lst[1][1]:
		return maxWord([lst[0]] + lst[2:])
	return maxWord(lst[1:])
 
def bestWord(Rack):
	'''returns the best possible word i.e. highest valued word based 
	off given Rack'''
	if Rack == []:
		return Rack
	return maxWord(scoreList(Rack))

# END