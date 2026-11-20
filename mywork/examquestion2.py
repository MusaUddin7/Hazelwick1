hours=-1
total=0
while hours!=0:
    hours=int(input("enter time parked in hours "))
    car=input("enter car type(electric or gas): ")
    if car=="electric":
        total=hours*2
        print("cost is",total,"pounds")
    elif car=="gas":
        total=hours*4
        print("cost is",total,"pounds")