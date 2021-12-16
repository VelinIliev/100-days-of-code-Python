height = int(input("enter your height in sm: "))/100
weight = int(input("enter your weight in kg: "))

BMI = round(weight/(height**2), 2)

print(f'Your BMI is {BMI}')

if BMI < 18.5:
    print("Your weight is: underweight")
elif BMI < 25:
    print("Your weight is: normal")
elif BMI < 30:
    print("Your weight is: overweight")
elif BMI < 35:
    print("Your weight is: obese")
else: 
    print("Your weight is: clinically obese")
