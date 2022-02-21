from selenium import webdriver
import time

PROMISE_DOWN = 150
PROMISE_UP = 10 
CHROME_DRIVER_PATH = "C:/Users/ngocc/Desktop/Web_dev/ChromeDriver/chromedriver"
TWITTER_EMAIL =""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(60)

        self.down = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.up = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
print(bot.up.text)
print(bot.down.text)