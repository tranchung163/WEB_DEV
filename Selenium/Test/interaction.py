from base64 import encode
from cgi import print_environ
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

chrome_driver_path = f"C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element_by_xpath("//*[@id='articlecount']/a[1]")

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)