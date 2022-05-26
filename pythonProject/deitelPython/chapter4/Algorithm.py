num = eval(input("Enter a number: "))
while num != 1:
    if num % 2 == 0:
        print('Number is Even')
        break

    if num % 2 != 0:
        print('Number is Odd')
        break

