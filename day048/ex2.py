from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url)

# articles = driver.find_element_by_css_selector('#articlecount a')
articles = driver.find_element_by_css_selector('a[Title="Special:Statistics"]')
print(articles.text)

# articles.click()

# all_portals = driver.find_element_by_partial_link_text("All portals")
# all_portals.click()

input = driver.find_element_by_name("search")
input.send_keys("python") 
# search_btn = driver.find_element_by_id("searchButton")
# search_btn.click()
input.send_keys(Keys.ENTER)


# driver.quit()