from selenium import webdriver

chrome_driver_path = "/Users/velin.iliev/Desktop/WDCourse/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.python.org/"
driver.get(url)

events = {}

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_text = driver.find_elements_by_css_selector(".event-widget .menu a")

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_text[n].text
    }

# for i in range(1, 6):
#     event_date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
#     event_text = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
#     events[i-1] = {
#         "time": event_date.get_attribute("datetime").split("T")[0],
#         "name": event_text.text
#     }
#     # print(event_date.get_attribute("datetime").split("T")[0], event_text.text)

print(events)
driver.close()