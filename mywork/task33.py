import random
number1=random.randint(1,100)
import random
number2=random.randint(1,100)
import random
number3=random.randint(1,100)
import random
number4=random.randint(1,100)
import random
number5=random.randint(1,100)
guessnumber1=int(input("enter a guess for number 1 "))
guessnumber2=int(input("enter a guess for number 2 "))
guessnumber3=int(input("enter a guess for number 3 "))
guessnumber4=int(input("enter a guess for number 4 "))
guessnumber5=int(input("enter a guess for number 5 "))


if (number1-guessnumber1)==0:
    print("bang on(1)")
elif (number1-guessnumber1)<=5 and (number1-guessnumber1)>=-5:
    print("close(1)")
elif (number1-guessnumber1)<=10 and (number1-guessnumber1)>=-10:
    print("okay(1)")
elif (number1-guessnumber1)>=11 and (number1-guessnumber1)<=-11:
    print("way off(1)")


if (number2-guessnumber2)==0:
    print("bang on(2)")
elif (number2-guessnumber2)<=5 and (number2-guessnumber2)>=-5:
    print("close(2)")
elif (number2-guessnumber2)<=10 and (number2-guessnumber2)>=-10:
    print("okay(2)")
elif (number2-guessnumber2)>=11 and (number2-guessnumber2)<=-11:
    print("way off(2)")


if (number3-guessnumber3)==0:
    print("bang on")
elif (number3-guessnumber3)<=5 and (number3-guessnumber3)>=-5:
    print("close")
elif (number3-guessnumber3)<=10 and (number3-guessnumber3)>=-10:
    print("okay")
elif (number3-guessnumber3)>=11 and (number3-guessnumber3)<=-11:
    print("way off")


if (number4-guessnumber4)==0:
    print("bang on(4)")
elif (number4-guessnumber4)<=5 and (number4-guessnumber4)>=-5:
    print("close(4)")
elif (number4-guessnumber4)<=10 and (number4-guessnumber4)>=-10:
    print("okay(4)")
elif (number4-guessnumber4)>=11 and (number4-guessnumber4)<=-11:
    print("way off(4)")


if (number5-guessnumber5)==0:
    print("bang on(5)")
elif (number5-guessnumber5)<=5 and (number5-guessnumber5)>=-5:
    print("close(5)")
elif (number5-guessnumber5)<=10 and (number5-guessnumber5)>=-10:
    print("okay(5)")
elif (number5-guessnumber5)>=11 and (number5-guessnumber5)<=-11:
    print("way off(5)")