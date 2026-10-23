A=0
B=0
C=0
total=0
vote=""
while vote!="End" and vote!="end":
    vote=input("Enter your vote:")
    if vote=="A" or vote=="a":
        A+=1
    elif vote=="B" or vote=="b":
        B+=1
    elif vote=="C" or vote=="c":
        C+=1
    else:
        print("Invalid vote")
print("Total votes for A:",A)
print("Total votes for B:",B)
print("Total votes for C:",C)
print("Total peoples who voted:",A+B+C)