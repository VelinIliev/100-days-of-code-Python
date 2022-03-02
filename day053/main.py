from selenium import webdriver
from time import sleep
import csv

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.zillow.com/san-francisco-ca/rentals/4-_beds/1.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.77253238085937%2C%22east%22%3A-122.10099307421875%2C%22south%22%3A37.55815045277765%2C%22north%22%3A38.11507472504167%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A826554%7D%2C%22beds%22%3A%7B%22min%22%3A4%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

driver.get(url)

sleep(2)

prices = driver.find_elements_by_class_name("list-card-price")
adresses = driver.find_elements_by_class_name("list-card-addr")

link_elements = driver.find_elements_by_css_selector(".list-card-link")
links = [link.get_attribute('href') for link in link_elements ]

header = ['adress', 'price', 'link']
rows = []

for x in range(len(prices)):
    row = [adresses[x].text, prices[x].text, links[x]]
    rows.append(row)
print(rows)

with open('data.csv', 'w', encoding='UTF8') as file:
    writer = csv.writer(file)

    writer.writerow(header)
    writer.writerows(rows)