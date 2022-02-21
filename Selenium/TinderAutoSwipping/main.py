from base64 import encode
from cgi import print_environ
from sre_constants import SUCCESS
from selenium import webdriver
import time

#Open Tinder website
chrome_driver_path = "C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")


#Login with Facebook account
log_in = driver.find_element_by_xpath("//*[@id='c-1420294622']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
log_in.click()
time.sleep(1)

log_in_gg = driver.find_element_by_xpath("//*[@id='c1146291598']/div/div/div[1]/div/div[3]/span/div[2]/button")
log_in_gg.click()
time.sleep(1)

base_window = driver.window_handles[0]
fb_login = driver.window_handles[1]
driver.switch_to.window(fb_login) #Switch to FB window
print(driver.title)
time.sleep(1)

email = driver.find_element_by_xpath("//*[@id='email']")
email.send_keys("")

password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys("")
time.sleep(1)

successful_log_in = driver.find_element_by_name("login")
successful_log_in.click()


#switch back to Tinder
driver.switch_to.window(base_window)



