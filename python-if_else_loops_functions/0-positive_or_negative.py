#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
a=int(input("enter number:"))
if a > 0:
    print("number is positive")
elif a == 0:
    print("number is zero")
else a < 0:
    print("number is negative")

