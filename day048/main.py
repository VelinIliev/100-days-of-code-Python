from selenium import webdriver

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# url = "https://www.amazon.com/dp/B08ZS28MT2/ref=syn_sd_onsite_desktop_268?psc=1&pd_rd_plhdr=t&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHNU1YTDVSVU1PWUomZW5jcnlwdGVkSWQ9QTAxMDA0MjFESjNUUldPNFJMTk4mZW5jcnlwdGVkQWRJZD1BMTAzMzM5MjJPUFhEMjc5VEJKS1Imd2lkZ2V0TmFtZT1zZF9vbnNpdGVfZGVza3RvcCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
url = "https://www.python.org/"
driver.get(url)


# title = driver.find_element_by_id("productTitle")
# print(title.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# link = driver.find_element_by_css_selector(".documentation-widget a")
# print(link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

driver.close()