print("Calculator")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

a = int(input("Enter number = "))
b = int(input("Enter another number = "))
choices = input("either + or - or * or / or % ")
if choices == "+":
    print(f"The sum of {a} and {b} is {add(a,b)}")
elif choices == "-":
    print(f"The sub of {a} and {b} is {sub(a,b)}")
elif choices == "*":
    print(f"The mul of {a} and {b} is {mul(a,b)}")
elif choices == "/":
    print(f"The div of {a} and {b} is {div(a,b)}")
elif choices == "%":
    print(f"The mod of {a} and {b} is {mod(a,b)}")
else:
    print("Please enter the giver operators")