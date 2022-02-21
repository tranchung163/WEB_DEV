from tkinter import Button
from numpy import single
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import lxml

GG_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfFt2hEAQSD9CV8P1y0iou_gDFr9RSNcBGulZ_O6gTTrIXd4Q/viewform?usp=sf_link"
CHROME_PATH = "C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"
ZILLOW_SEARCH = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56162921732572%2C%22east%22%3A-122.3393620580649%2C%22south%22%3A37.710650785126305%2C%22north%22%3A37.812758503028924%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A803028%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US"
}
response = requests.get(url=ZILLOW_SEARCH, headers=headers).text
soup = BeautifulSoup(response, "lxml")

zillow_links_element = soup.select(".list-card-info a")
zillow_links = []
for link in zillow_links_element:
    href = link["href"]
    if "http" in href:
        zillow_links.append(href)
    else:
        zillow_links.append(f"htpps://www.zillow.com{href}")

address_elements = soup.find_all(name="address", class_="list-card-addr")
addresses = [address.text for address in address_elements]

price_elements = soup.find_all(name="div", class_="list-card-price")
prices = [int(price.text[1:6].replace(",","")) for price in price_elements]

driver = webdriver.Chrome(executable_path=CHROME_PATH)

for n in range(len(zillow_links)):
    driver.get(GG_FORM_LINK)
    time.sleep(2)
    address = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address.send_keys(addresses[n])

    price = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price.send_keys(prices[n])

    link = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link.send_keys(zillow_links[n])

    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit_button.click()



