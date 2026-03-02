"""Write a python program that outputs all possible strings formed by using charcters 
c a t d o g exacty once"""

import itertools

# Define the characters
chars = "catdog"

# Generate all permutations
permutations = itertools.permutations(chars)

# Print each permutation as a string
for p in permutations:
    print("".join(p))
    
