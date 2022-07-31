num = 1
while num <= 100:
    if num % 15 == 0:
        print("FIZZ BUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    elif num % 5 == 0:
        print("BUZZ")
    else:
        print(num)
    num += 1

