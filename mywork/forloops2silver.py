total=0
highest=0
frostydays=0
days=int(input("Enter number of days: "))
for i in range(1,days+1):
    print("Day",i)
    temperature=float(input("Enter temperature: "))
    total+=temperature
    if temperature > highest:
        highest= temperature
    elif temperature<0:
        frostydays+=1
averagetemperature=total/days
print("Average temperature: ", averagetemperature)
print("Highest temperature: ", highest)
print("Frosty days: ", frostydays)