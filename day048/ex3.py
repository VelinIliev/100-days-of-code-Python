from selenium import webdriver

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Velin")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Iliev")

email = driver.find_element_by_name("email")
email.send_keys("xxxxxx@xxx.com")

submit = driver.find_element_by_css_selector("button")
submit.click()
