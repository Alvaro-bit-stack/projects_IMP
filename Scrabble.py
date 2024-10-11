'''
Created on 10/4/2024
@author:   Alvaro Izquierdo and Marlene Moranchel
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    '''
Returns the score of the given letter
    '''
    if scorelist ==  []:
        return 0
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(s, scorelist):
    '''
Calculates the total score of a given word 
    '''
    if s == '':
        return 0
    else:
        return letterScore(s[0],scorelist) + wordScore(s[1:],scorelist)

def scoreList(Rack):
    '''
calculates all the words that can be made from a given rack of letters
    '''
    return list(map(lambda lst1,lst2: [lst1,lst2],list(filter(lambda x: word_in_rack(x, Rack), Dictionary)),list(map(lambda s: wordScore(s,scrabbleScores), list(filter(lambda x: word_in_rack(x, Rack), Dictionary))))))

def word_in_rack(word,Rack):
    '''
Helper function that checks every letter in a word to make sure its part of the Rack
    '''
    if len(word) == 1 and word in Rack:
        return True
    elif word[0] in Rack:
        return word_in_rack(word[1:], Rack[:Rack.index(word[0])] + Rack[Rack.index(word[0])+1:])
    else:
        return False
def findMax(lst):
    '''
Comapres each word to each other which could be made out of a given rack to find the word with the highest score 
    '''
    if lst == []:
        return ['',0]
    if len(lst) == 1:
        return [lst[0][0],lst[0][1]]
    elif lst[0][1] > lst[-1][1]:
        return findMax(lst[0:-1])
    else:
        return findMax(lst[1:])

def bestWord(Rack):
    '''
Finds the best word with the highest score 
    '''
    return findMax(scoreList(Rack))
    

