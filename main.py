from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = "90"
PROMISED_UP = "10"
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""

CHROME_DRIVER_PATH = "/Users/me/Documents/development/chromedriver"
SERVICE = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        self.go_button = self.driver.find_element(By.CLASS_NAME, 'test-mode-multi')
        self.go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        print(self.down.text)
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        print(self.up.text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        time.sleep(3)
        self.login = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        self.login.click()

        time.sleep(3)
        # self.base_window = self.driver_handles[0]
        # self.login_window = self.driver_handles[1]
        # self.driver.switch_to.window(self.login_window)
        # print(self.driver.title)
        self.username_field = self.driver.find_element(By.NAME, "text")
        self.username_field.send_keys(TWITTER_USERNAME)
        self.username_field.send_keys(Keys.ENTER)

        time.sleep(3)
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.password_field.send_keys(TWITTER_PASSWORD)
        self.password_field.send_keys(Keys.ENTER)

        time.sleep(3)
        self.compose_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        self.compose_tweet.click()

        time.sleep(3)
        self.write_message = self.driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
        self.write_message.send_keys(f"Python bot test\ndown:{self.down}\nup:{self.up}")

        time.sleep(3)
        self.publish = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        self.publish.click()




bot = InternetSpeedTwitterBot(SERVICE)

bot.get_internet_speed()
bot.tweet_at_provider()