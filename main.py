from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

# SINGULAR
# search_bar = driver.find_element(By.NAME, "q")
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")

#Using xpath
#find = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(find.text)

#PLURAL
# find_elements
# SCRAPING from python.org
# list_of_times = []
# list_of_events = []
# times = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
# for x in times:
#     list_of_times.append(x.text)
# events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
# for x in events:
#     list_of_events.append(x.text)
# dic = {i: {'Time': list_of_times[i], 'Event': list_of_events[i]} for i in range(5)}
# print(dic)

# ________________________________________________________________________________

# SCRAPING FROM
driver.quit()
