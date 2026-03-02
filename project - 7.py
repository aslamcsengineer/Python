# -*- coding: utf-8 -*-
"""
Write a python program that inputs a list of words,separated by whitespace, and outputs how many 
times each word appears in the list. You need not appear about efficienct at this point,as this
topic is something that will be addressed later in this book
"""

a = input("Enter word separated by white spaces = ").split()
for i in set(a):
    print("word = ",i, a.count(i),"times")
