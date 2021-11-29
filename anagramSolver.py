#!/usr/bin/env python

import random
import itertools
import os

# Scrambles the letters of the given word.
def scrambleWord(toScramble):
    scrambled = list(toScramble)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Creates all permutations of the given word and stores it in an array.
def create_permutations(word):
    permutations = ["".join(perm) for perm in itertools.permutations(word)]
    return permutations

# Searches for substrings of the word in the dictionary
def has_substrings(anagram, dictionary):
    for words in dictionary:
        if anagram == words:
            print (anagram)
            return True
    return False

# Simply counts all lines in the dictionary
def count_lines(dictionary):
    count = 0
    for line in dictionary:
        count +=1
        print(f"line {count}: {line}")


while True:
    
    # Tests
    """ print (dictionary) """
    """ print ("Scrambled word:", scrambleWord(anagram)) """
    """ print (createPermutations(anagram)) """

    # TODO: Make program combine all .txt files in one dictionary
    """ word_path = "words/"
    all_files = os.listdir(word_path)
    print (all_files)

    for filename in all_files:
        if filename.endswith(".txt"):
            with open(word_path + filename) as file:
                dictionary = file.read().splitlines() """

    with open("words/wlist_match2.txt") as file:
        dictionary = file.read().splitlines()
    
    """ count_lines(dictionary) """
    
    anagram = input("Enter the anagram to be solved: ")
    scrambled = scrambleWord(anagram)
    permutations = create_permutations(anagram)
    
    print (set(permutations) & set(dictionary))

    break