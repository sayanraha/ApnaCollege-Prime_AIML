'''
Let’s create a “Number guessing game”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:

• "Too high" - > if the guess is above the number

• "Too low" -> if the guess is below the number

• "Correct" ->  if the guess matches

'''
import random

randValue = random.randint(1,100) # for genrating random value from 1 - 100


while True:
    guess = int(input("enter a number : "))

    if guess == randValue:
        print("Correct")
        break
    elif guess < randValue:
        print("Too Low")
    elif guess > randValue:
        print("Too high")

print("Program ended.")