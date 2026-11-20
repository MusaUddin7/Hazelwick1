import random
num = random.randint(1, 100)

for count in range (10):
    guess = int(input("Enter a guess: "))

    if guess < 1 or guess > 100:
        print("Not in range, range is 1-100")
    if guess == num:
        print("You win!")
        break
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
else:
    print("Out of guesses, it was", num)