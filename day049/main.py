from selenium import webdriver

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python"
driver.get(url)


sign_in_btn = driver.find_element_by_class_name("nav__button-secondary")
sign_in_btn.click()


username = driver.find_element_by_id("username")
username.send_keys("veliniliev")

password = driver.find_element_by_id("password")
password.send_keys("alsdkjlaksjd")

sign_in_btn2 = driver.find_element_by_css_selector('[data-litms-control-urn="login-submit"]')
sign_in_btn2.click()