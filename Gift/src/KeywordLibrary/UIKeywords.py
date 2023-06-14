import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options


class ui_keywords:
    def __init__(self):
        self.browser = ""
        self.driver = ""

    def get_browser1(self):
        my_service = Service('Gift/lib/chromedriver.exe')
        self.browser = webdriver.Chrome(service=my_service)
        return self.browser

    def get_browser(self, browser_type):
        options = Options()
        if browser_type == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            my_service = Service('Gift/lib/chromedriver.exe')
            self.driver = webdriver.Chrome(service=my_service, options=options)
            print("Entered browser is chrome")
        elif browser_type == "firefox":
            options.add_argument("--headless")
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            my_service = Service('Gift/lib/geckodriver.exe')
            self.driver = webdriver.Firefox(service=my_service, options=options)
            print("Entered browser is firefox")
        else:
            print("Browser not specified")

        return self.driver

    def open_browser(self, url, browser_type, user, passwd):
        self.browser = self.get_browser(browser_type)
        self.browser.get(url)
        return self.browser

    def clean_browser(self):
        time.sleep(5)
        self.browser.quit()
