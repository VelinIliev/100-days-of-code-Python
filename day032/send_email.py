# Gmail: smtp.gmail.com
# SMTP = Simple Mail Transfer Portocol

# Manage yor account -> Securty
    # Signing in to Google
        # Use your phone to sign in : OFF
        # 2-Step Verification: OFF
    # Less secure app access
        # Allow less secure apps: ON

import smtplib

my_email = "********@gmail.com"
password = "*********"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="*********@yahoo.com", msg="Subject:Hello\n\nHello, Velin. \nHow are you today?.")

