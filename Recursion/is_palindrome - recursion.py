#check palindrome or not using recursion 

def is_paliondrome(s,start,stop):
    if(start>=stop):
        return True
    if(s[start]==s[stop]):
        return is_paliondrome(s, start+1, stop-1)
    else:
        return False 
    
print(is_paliondrome("racecar", 0, len("racecar")-1))
