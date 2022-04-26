import random
number = random.randint(1,59)
chances = 0

while chances<5:
    guess=int(input("Enter a number"))
    if (guess==number):
        print("you won!")
    elif guess<number:
        print("your guess is too low")
    else: 
        print("your guess is too high")

    chances = chances+1