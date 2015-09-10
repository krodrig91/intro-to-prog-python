'''
Created on Feb 12, 2015
@author: Kelvin Rodriguez
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    '''returns the minimum number of coins needed to add up to amount
    using the given coins list and the coins needed'''
    if amount == 0: return [0,[]]
    elif coins == []: return [float("inf"),[]]
    elif amount < coins[0]: return giveChange(amount, coins[1:])
    else:
        use_it = giveChange(amount - coins[0], coins)
        use_it = [use_it[0] + 1, use_it[1] + [coins[0]]]
        lose_it = giveChange(amount, coins[1:])
    if use_it[0] < lose_it[0]: return use_it
    else: return lose_it

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# helper functions for wordsWithScore()
def letterScore(letter, scorelist):
    '''returns the score associated with letter in scorelist.'''
    if letter == '': return "You didn't enter a letter." # ignores other data types
    elif letter == scorelist[0][0]: return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''returns the score associated with string S based off scorelist.'''
    if S == '': return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list off words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, Dictionary) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return map(lambda word : [word, wordScore(word, scores)], dct)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# function assumes n >= 0
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0: return []
    elif n > len(L): return L
    else: return [L[0]] + take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# function assumes n >= 0
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0: return L
    elif n > len(L): return []
    return drop(n-1, L[1:])

# END