# reverse using recursion

def reverse(seq,start,stop):
    if start<stop-1:
        seq[start],seq[stop-1] = seq[stop-1],seq[start]
        reverse(seq, start+1, stop-1)
    return seq 
a = [1,2,3]
r = reverse(a, 0, 3)
print(r)
        
