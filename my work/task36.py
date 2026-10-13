count=0
import random
number = random.randint(1, 100)
guess=int(input("Guess a number between 1 and 100()10 attempts: "))
while guess != number and count < 10:
    if guess < number:
        print("Too low!")
    elif guess== number:
        print("You guessed it!")
        break
    
    else:
        print("Too high!")
    guess=int(input("Guess again: "))
count += 1
print(" You didnt guess the number! It was", number)