#!/usr/bin/env python

import random

def scrambleWord(toScramble):
    scrambled = list(toScramble)
    random.shuffle(scrambled)
    return ''.join(scrambled)



while True:
    anagram = raw_input("Enter the anagram to be solved: ")
    print (scrambleWord(anagram))
    break