import KeywordLibrary.UIKeywords

uk = KeywordLibrary.UIKeywords.ui_keywords()
url = 'https://www.google.com'
title = uk.launch_ui(url, 'abc', 'bcd')
print(title)
