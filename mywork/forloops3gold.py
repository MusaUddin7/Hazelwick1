count=0
targettotal=int(input("Enter a target total (2,12)"))
for dice1 in range (1,7):
    for dice2 in range (1,7):
        if targettotal == dice1 + dice2:
            print(dice1, " + ", dice2)
            count+=1
print("There are",count,"ways to roll", targettotal)
print("That is",count, "out of 36")