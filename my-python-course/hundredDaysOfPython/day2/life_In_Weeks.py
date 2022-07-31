print("Life In Weeks Calculator")

age = int(input("What is your current age: \n"))

daysRemaining = 32850 - (age * 365)
weeksRemaining = 4680 - (age * 52)
monthsRemaining = 1080 - (age * 12)

print(f"You have {daysRemaining} days, {weeksRemaining} weeks and {monthsRemaining} months left")
