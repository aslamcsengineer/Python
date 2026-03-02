
"""
A common punishment for school children is to write out a sentence multiple times. Write a 
python stand alone program that will write out the following sentence one hundread times.
"I will never spam my friends again". Your program should number each sentences and it should
make eight different random looking typos
"""

import random

sentence = "I will never spam my friends again"

# pick 8 random line numbers where typos will appear
typo_lines = random.sample(range(1, 101), 8)

for i in range(1, 101):
    text = sentence
    if i in typo_lines:
        pos = random.randint(0, len(sentence)-1)   # random position
        text = sentence[:pos] + random.choice("abcdefghijklmnopqrstuvwxyz") + sentence[pos+1:]
    print(f"{i}. {text}")