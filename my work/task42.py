count=0
import random
num=random.randint(1,100)
while True:
    guess=int(input("Enter a guess"))
    count+=1
    if guess > num:
        print ("too high")
    elif guess < num:
        print ("too low")
    elif guess >100 or guess<0 :
        print ("not in range, range is 1-100")
        count-=1
    if count =10 :
        print("out of guesses, it was" + num)
    elif num=guess
        print("You win!")