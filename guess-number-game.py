import random

print("welcome to this game")
a = int(input("enter the first number of range: "))
b = int(input("enter the second number of range: "))
n = random.randint(a, b)
print("I choose a number between", a, "to", b)

while(True):
    g = int(input("guess: "))
    if(g == n):
        print("you win")
        break
    elif(g < n):
        print("enter bigger number")
    else:
        print("enter lower number")



