from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_browser():
    service = Service('Gift/lib/chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    return browser


def launch_ui(url, user, passwd):
    browser = get_browser()
    browser.get(url)
    print(browser.title)
    print(browser.title)


url = 'https://www.google.com'
launch_ui(url, 'a', 'b')
