# -*- coding: utf-8 -*-
#Base two logarithm 

def find_log(n,log_val):
    if(n//2==0):
        return log_val 
    else:
        log_val+=1 
        return find_log(n/2, log_val)
print(find_log(1000, 0))
