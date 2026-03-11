#array even first odd second 

def even_odd(seq,left,right):
    if(left>=right):
        return seq
    if(seq[left]%2==0):
        return even_odd(seq, left+1, right)
    elif(seq[right]%2!=0):
        return even_odd(seq, left, right-1)
    else:
        seq[left],seq[right] = seq[right],seq[left]
        return even_odd(seq, left+1, right-1)
    
a = [1,3,4,5,6,7,8]
print(even_odd(a, 0, len(a)-1))