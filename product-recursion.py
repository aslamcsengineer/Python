# Calculate product num1 and num2 using only addition and subtraction 

def product(n1,n2,value = 0):
    if(n2==0):
        return value 
    else:
        n2-=1 
        value+=n1 
        return product(n1, n2,value)
print(product(3, 6))
