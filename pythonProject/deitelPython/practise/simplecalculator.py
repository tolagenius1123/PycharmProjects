num1 = int(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = int(input("Enter a second number: "))

if operator == "+":
    print("Sum of ", num1, " and ", num2, " = ", num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "//":
    print(num1 / num2)
else:
    print("Invalid operator")
