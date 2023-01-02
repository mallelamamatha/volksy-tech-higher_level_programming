#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
a=int(input("enter number:"))
if a > 0:
    print("positive")
elif a == 0:
    print("zero")
else a < 0:
    print("negative")

