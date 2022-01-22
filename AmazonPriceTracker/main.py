from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os


YOUR_EMAIL = os.environ.get("YOUR_EMAIL")
YOUR_PASSWORD = os.environ.get("YOUR_PASSWORD")
PRODUCT_URL = "https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=zg_bs_5_3/143-8330487-8424453?pd_rd_i=0984782850&psc=1"
print(YOUR_EMAIL)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US"
}
response = requests.get(url=PRODUCT_URL, headers=headers).text

soup = BeautifulSoup(response, "lxml")
product_price = float(soup.find(name="span", id="newBuyBoxPrice").getText()[1:])
product_title = soup.find(name="span", id="productTitle").getText()

if product_price < 18:
    message = f"{product_title} is now {product_price}"
    with smtplib.SMTP("Smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL,YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs="tranchung163@gmail.com",
            msg=f"Subject: Amazon price alert! \m\m{message}\n{PRODUCT_URL}"
        )