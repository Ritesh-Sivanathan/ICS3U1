'''
Name: Ritesh Sivanathan
Date: March 17th, 2025
Description: Guess a random number
'''

import random

correct = random.randint(0, 100)
a = int(input())

while a != correct:
    a = int(input())
    print(f"Your guess of {a} is incorrect :(")
