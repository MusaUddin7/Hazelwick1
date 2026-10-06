side1 = int(input("Enter the first side length: "))
side2 = int(input("Enter the second side length: "))
side3 = int(input("Enter the third side length: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
	print("These lengths cannot make a triangle.")
elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
	print("These lengths cannot make a triangle.")
elif side1 == side2 == side3:
	print("This is an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
	print("This is an isosceles triangle.")
else:
	print("This is a scalene triangle.")
