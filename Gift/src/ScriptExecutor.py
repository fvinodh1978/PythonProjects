import KeywordLibrary.UIKeywords
import JsonUtils1
from Gift.Utils import JsonUtils

ui = KeywordLibrary.UIKeywords.ui_keywords()
url = JsonUtils.get_env("url")
mybrowser = JsonUtils.get_env("browser")
browser = ui.open_browser(url, mybrowser, 'abc', 'bcd')
print(browser.title)
ui.clean_browser()
