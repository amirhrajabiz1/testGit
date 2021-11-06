import random

print("welcome to this game")
n = random.randint(1, 30)
print("I choose a number between 1 to 30")

while(True):
    g = int(input("guess: "))
    if(g == n):
        print("you win")
        break
    elif(g < n):
        print("enter bigger number")
    else:
        print("enter lower number")



