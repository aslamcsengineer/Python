# ackerman problem

'''let m be first number and n be second number

rule 1 if m=0 then add 1 to n
rule 2 if m>0 and n=0 then m -= 1 and n = 1
rule 3 if m>0 and n>0 then m-=1 and n = function(m ,n-1)'''

def ackermann(m, n):
    # Rule 1: The Easy One (m is 0)
    # We just add 1 to n and give the answer back.
    if m == 0:
        return n + 1
    
    # Rule 2: The Reset (m is > 0, but n is 0)
    # We subtract 1 from m, and change n to 1.
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    
    # Rule 3: The Monster (Both m and n are > 0)
    # We subtract 1 from m, and put a whole new ackermann function inside for n.
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Let's test it with the exact example we just walked through!
result = ackermann(1, 1)
print(f"The result of A(1, 1) is: {result}")