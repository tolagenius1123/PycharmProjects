num = 1
while num != -1:
    num = int(input("Guess a number: "))
    if num == 15:
        print("You got it right")
        break
    elif num < 15:
        print("Oops! Try again")
    elif num > 15:
        print('try again')
        num += 1

