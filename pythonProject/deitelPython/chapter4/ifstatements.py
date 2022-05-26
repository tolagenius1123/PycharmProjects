print("****************************")
print(" Welcome to StudentGradeApp")
print("****************************")
name = input("Enter Student name:")
score = eval(input("Enter Student's score:"))
print("****************************")

if score >= 75:
    print("Excellent!", name, "got an A")
elif score >= 65:
    print("Good job! You got a B")
elif score >= 50:
    print("Nice! You got a C")
else:
    print("Opps! You failed the test")
print("****************************")
