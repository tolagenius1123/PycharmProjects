num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))


def divide(num, den):
    pass


while True:
    try:
        print(divide(num, den))
        break
    except ValueError:
        print("Wrong value")
        num = int(input("Enter the numerator: "))
        den = int(input("Enter the denominator: "))
