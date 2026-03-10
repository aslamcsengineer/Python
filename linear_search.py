# linear search


def linear_search(a,element):
    for i in range(len(a)):
        if(a[i]==element):
            return i
    return -1 

a = [1,2,3,4,5]
x = 3
found = linear_search(a, x)

if(found==-1):
    print("Not found")
else:
    print("element found at index = ",found)
    
#Best case = O(1)
#Worst case = O(n)