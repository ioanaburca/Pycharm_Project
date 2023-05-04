from selenium import webdriver

chrome = webdriver.Chrome() # deschidem browserul

# navigam catre un url
chrome.get("https://formy-project.herokuapp.com/form")

actual = chrome.current_url
expected = 'https://formy-project.herokuapp.com/form2'

assert actual == expected, f"invalid url"

print("TEST PASSED")