from base64 import encode
from cgi import print_environ
from selenium import webdriver


chrome_driver_path = f"C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.billboard.com/charts/hot-100/2019-01-01")

#times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_id("title-of-a-story")

a_hundred_songs = [name.text for name in event_names]
new_list = []
for name in a_hundred_songs:
    if name != "":
        new_list.append(name)
print(new_list[0:100])   


