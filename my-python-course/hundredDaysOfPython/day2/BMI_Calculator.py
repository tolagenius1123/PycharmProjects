weight = eval(input("Enter your weight in kg: \n"))
height = float(input("Enter your height in m: \n"))

BMI = weight / height ** 2
print(int(BMI))