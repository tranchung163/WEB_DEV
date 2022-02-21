from base64 import encode
from cgi import print_environ
from selenium import webdriver


chrome_driver_path = f"C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

event_times_list = [time.text for time in times]
event_names_list = [name.text for name in event_names] 

events = {}

for n in range(len(event_times_list)):
    events[n] = {
        "time": event_times_list[n],
        "name": event_names_list[n]
    }

print(events)





