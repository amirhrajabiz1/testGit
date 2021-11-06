import random
import time

start_time = time.time()

print("welcome to this game")
a = int(input("enter the first number of range: "))
b = int(input("enter the second number of range: "))
n = random.randint(a, b)
print("I choose a number between", a, "to", b)

step = 0
while(True):
    g = int(input("guess: "))
    step += 1
    if(g == n):
        print("you win")
        break
    elif(g < n):
        print("enter bigger number")
    else:
        print("enter lower number")
end_time = time.time()

t = end_time - start_time
print("your game takes %.2f second(s)" %(t))

score = (b * 2) / (t * 3 + step * 4)
print("your score is: %.2f" %score)
