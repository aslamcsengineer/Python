# -*- coding: utf-8 -*-
"""
The birthday paradox says that the probability that two people in a room will have the same
birthday is more than half,provided n,the number of people in the room, is more then 23. This 
property is not really a paradox, but many people find it suprising. Design a python program
that test this paradox by a series of experiments on randomly generated birthdays, which test
this paradox for n = 5,10,15,20,...,100
"""

import random

trials = 1000   # number of experiments

for n in range(5, 101, 5):   # group sizes: 5, 10, 15, ..., 100
    count = 0
    for _ in range(trials):
        birthdays = []
        for _ in range(n):
            day = random.randint(1, 365)   # random birthday
            birthdays.append(day)
        # check if duplicate exists
        if len(birthdays) != len(set(birthdays)):
            count += 1
    probability = count / trials
    print("Group size:", n, "-> Probability:", round(probability, 3))