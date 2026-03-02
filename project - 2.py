# -*- coding: utf-8 -*-
'''Write a python porgram that can take positve integer greater than 2 and write out 
number of times one must repeatedly divide this number by 2 before getting a value
less than 2 '''

a = int(input("Enter num = "))
c = 0
if(a>2):
    while(a>=2):
        a = a/2 
        c+=1 
    print(c)
else:
    print("Enter value > 2")