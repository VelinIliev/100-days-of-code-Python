# 🚨 Don't change the code below 👇
height = int(input("enter your height in sm: "))/100
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight/(height**2), 2)

print(f'Your BMI is {BMI}')