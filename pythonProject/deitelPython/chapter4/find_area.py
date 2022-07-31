import math

radius = eval(input("Enter radius: "))

if radius < 0:
    print("Invalid input")
else:
    area = radius * radius * 3.142  # math.pi
    print("The area of the shape is", area)
