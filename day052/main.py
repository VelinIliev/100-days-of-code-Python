from selenium import webdriver
from time import sleep

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.facebook.com/messages/t/********"

driver.get(url)

sleep(2)

allow = driver.find_element_by_css_selector('[title="Allow Essential and Optional Cookies"]')
allow.click()

sleep(1)
email = driver.find_element_by_id("email")
email.send_keys('****************')

password = driver.find_element_by_id("pass")
password.send_keys("*************")

login_btn = driver.find_element_by_id('loginbutton')
login_btn.click()

messageFB = driver.find_element_by_css_selector('[aria-label="Съобщение"] p')
messageFB.send_keys("Hi")