#!/usr/bin/env python

import random
import itertools

# Scrambles the letters of the given word.
def scrambleWord(toScramble):
    scrambled = list(toScramble)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Creates all permutations of the given word and stores it in an array.
def createPermutations(word):
    permutations = ["".join(perm) for perm in itertools.permutations(word)]
    return permutations

while True:
    anagram = input("Enter the anagram to be solved: ")
    """ print ("Scrambled word:", scrambleWord(anagram)) """

    print (createPermutations(anagram))
    break