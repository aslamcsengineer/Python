"""
Write a python program that simulates a handheld calculator.Your Program should process input 
from the python console representing buttons that are pushed and then output the contents
of the screen after each operations is performed.Minmally, your calculator should be able to process
the basic arithemetic operations and rest/clear operation
"""

def calculator():
    print("Simple Calculator. Enter Q to quit, C to clear.")
    screen = 0
    current = ""
    
    while True:
        button = input("Enter button: ")
        
        if button.upper() == "Q":
            print("Calculator exited")
            break
        elif button.upper() == "C":
            screen = 0
            current = ""
            print("Screen cleared")
        elif button == "=":
            try:
                screen = eval(current)   # evaluate the expression
                print("Screen:", screen)
                current = str(screen)    # keep result for next operation
            except:
                print("Error")
                current = ""
        else:
            current += button
            print("Screen:", current)

calculator()