#linear recursion 
def linear_sum(a,n):
    if(n==0):
        return 0 
    else:
        return linear_sum(a,n-1)+a[n-1] 

print(linear_sum([1,2,3],3))

#O(n)