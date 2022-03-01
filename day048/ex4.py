from selenium import webdriver

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie = driver.find_element_by_id("cookie")


for x in range(1000):
    cookie.click()