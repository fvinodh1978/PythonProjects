from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ui_keywords:
    def __init__(self):
        pass

    def get_browser(self):
        service = Service('Gift/lib/chromedriver.exe')
        browser = webdriver.Chrome(service=service)
        return browser

    def launch_ui(self, url, user, passwd):
        browser = self.get_browser()
        browser.get(url)
        title = browser.title
        return title
