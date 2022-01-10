import pandas
import datetime as dt
import random
import smtplib


##################### Extra Hard Starting Project ######################

MY_EMAIL = "********@gmail.com"
MY_PASSWORD = "*********"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = dt.datetime.now()
birthdays = []

# 1. Update the birthdays.csv

try:
    data = pandas.read_csv("./birthdays.csv")
    birthdays = data.to_dict(orient='records')
except FileNotFoundError:
    print("no records yet")
    

new_birthday = input("Do you wanna to enter new birthday? y or n: ").lower()

if new_birthday == "y":
    name_input = input("Enrer name: ")
    email_input = input("Enrer email: ")
    year_input = input("Enrer year: ")
    month_input = input("Enrer month: ")
    day_input = input("Enrer day: ")

    new_entry = {
        'name': name_input,
        'email': email_input,
        'year': year_input,
        'month': month_input,
        'day': day_input
    }
    birthdays.append(new_entry)
    data = pandas.DataFrame(birthdays)
    data.to_csv("./birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv

today_birthdays = [ record for record in birthdays if record['month'] == now.month and record['day'] == now.day] 

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


if len(today_birthdays) > 0:
    
    for born_today in today_birthdays:

        random_letter = random.choice(LETTERS)

        with open(f"./letter_templates/{random_letter}", mode = "r") as file:
            contents = file.read()
            name = (born_today['name']).title()
            birthday_wish = contents.replace("[NAME]", name)
            print(birthday_wish)

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            email = born_today['email']
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{birthday_wish}")







