from selenium import webdriver
from time import sleep

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.speedtest.net/"

driver.get(url)

consent = driver.find_element_by_id("_evidon-banner-acceptbutton")
consent.click()

sleep(2)

start_btn = driver.find_element_by_class_name("js-start-test")
start_btn.click()

sleep(60)

download = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

print(f'Download Speed: {download.text} Mbps, Upload Speed: {upload.text} Mbps')

driver.quit()