import datetime as dt
import random
import smtplib

my_email = "********@gmail.com"
my_password = "*********"

now = dt.datetime.now()

if now.weekday() == 0:
    with open("./quotes.txt", mode = "r") as file:
        contents = file.readlines()
        monday_message = random.choice(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="*********@yahoo.com", msg=f"Subject:Monday Motivation\n\n{monday_message}")





