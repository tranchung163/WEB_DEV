from ast import Try
from selenium import webdriver
import time
import os

URL = "https://www.linkedin.com/jobs/search/?geoId=102095887&keywords=python%20developer&location=California%2C%20United%20States"
chrome_driver_path = "C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
sign_in_button.click()

user_name = driver.find_element_by_id("username")
user_name.send_keys("")

password = driver.find_element_by_id("password")
password.send_keys("")

sign_in = driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
sign_in.click()



all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
for listing in all_listings:
    print(listing.text)
    listing.click()
    time.sleep(3)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply")
        apply_button.click()


        phone = driver.find_element_by_class_name("fb-single-line-text")
        if phone.text == "":
            phone.send_keys("123456789")
        next_button = driver.find_element_by_class_name("artdeco-button")
        while next_button:
            next_button.click()
    except:
        continue