from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('Gift/lib/chromedriver.exe')
browser = webdriver.Chrome(service=service)
url = 'https://www.google.com'
browser.get(url)
print(browser.title)