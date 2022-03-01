import requests
from bs4 import BeautifulSoup
import lxml
import smtplib



url = "https://www.amazon.com/dp/B08ZS28MT2/ref=syn_sd_onsite_desktop_268?psc=1&pd_rd_plhdr=t&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHNU1YTDVSVU1PWUomZW5jcnlwdGVkSWQ9QTAxMDA0MjFESjNUUldPNFJMTk4mZW5jcnlwdGVkQWRJZD1BMTAzMzM5MjJPUFhEMjc5VEJKS1Imd2lkZ2V0TmFtZT1zZF9vbnNpdGVfZGVza3RvcCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").text
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# send email
if price_as_float < 100:

    my_email = "velko2022@gmail.com"
    password = "Alabala10"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs="veliniliev@gmail.com", msg=f"Subject:Hello\n\n{price_as_float}.")

