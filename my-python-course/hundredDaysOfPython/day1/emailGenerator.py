import random

print("===========================")
print("Welcome to E-mail Generator")
print("===========================")

firstName = input("Enter your firstname: \n")
lastName = input("Enter your lastname: \n")
randomDigits = random.randint(1000, 2000)

print(f"Your email is {firstName}{lastName}{randomDigits}@gmail.com")
