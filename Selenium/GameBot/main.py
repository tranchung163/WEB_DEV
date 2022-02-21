from base64 import encode
from cgi import print_environ
from selenium import webdriver
import time 


chrome_driver_path = f"C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5

big_cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
items_ids = [item.get_attribute("id") for item in items]

while True:
    big_cookie.click()
    

    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)


        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]]=items_ids[n]


        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)


        affordable_upgrade = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = id


        highest_price_affordable_upgrade = max(affordable_upgrade)
        to_purchase_id = affordable_upgrade[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5
        
        if time.time() > five_min:
            break





