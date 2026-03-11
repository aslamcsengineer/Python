#fibonacci

def gen_fib(length):
    if(length<=1):
        return 1
    else:
        return gen_fib(length-1)+gen_fib(length-2)
    
a = 5
print("Fibonaaci series")

for i in range(a):
    print(gen_fib(i))
