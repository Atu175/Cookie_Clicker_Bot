from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
# TEST
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # clicking
# # article_count.click()
# Wiktionary = driver.find_element(By.LINK_TEXT, "Wiktionary")
# # Wiktionary.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# # Use a non letter key
# search.send_keys(Keys.ENTER)

# CLICKING SIGN UP
driver.get("http://secure-retreat-92358.herokuapp.com/")
first = driver.find_element(By.NAME, "fName")
second = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
btn = driver.find_element(By.XPATH, '/html/body/form/button')
first.send_keys("Julian")
second.send_keys("Macoveski")
email.send_keys("macovaskij@hala.com")
btn.click()



