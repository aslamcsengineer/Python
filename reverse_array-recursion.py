# reverse using recursion

def reverse(a,start,stop):
    if(start<stop-1):
        a[start],a[stop-1] = a[stop-1],a[start]
        reverse(a, start+1, stop-1)
    return a
a = reverse([1,2,3],0,3)
print(a)
        
