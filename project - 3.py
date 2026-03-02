
"""
Write a python program that can ""make change". Your Program shoukd take two numbers as input,
One that is a monetary amount charges and other that is monetary amount given. It should then
return the number of each kind of bill and coin to give back as change for the difference between
the amount given and amount charged.The values assigned to the bills and coins can be based on
current denominations in use.Try to design a program so that it returns as few bills and coins as possible
"""

a = int(input("Enter bill = "))
b = int(input("Enter the given = "))
balance = b - a
print("Change = ", balance)

denominations = [500, 200, 100, 50, 20, 10, 5, 1]
coins = 0
result = {}

for d in denominations:
    if balance >= d:
        count = balance // d   # how many of this denomination
        balance = balance % d  # reduce balance
        coins += count
        result[d] = count

print("Total notes/coins = ", coins)
print("Denominations used:")
for k, v in result.items():
    print(f"{k} : {v}")

