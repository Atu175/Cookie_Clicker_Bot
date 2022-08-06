from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

import time
second = time.time() + 5
timeout = time.time() + 60*5   # 5 minutes from now
while True:
    cookie.click()
    if time.time() > second:
        # For cursor
        cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
        cursor_no = int(cursor.text.split()[2])
        cursor_btn = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
        # For grandma
        grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
        grandma_no = int(grandma.text.split()[2])
        grandma_btn = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
        # For factory
        factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
        factory_no = int(factory.text.split()[2])
        factory_btn = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
        # For mine
        mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
        mine_no = int(mine.text.split()[2].replace(",", ""))
        mine_btn = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
        # For shipment
        shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
        shipment_no = int(shipment.text.split()[2].replace(",", ""))
        shipment_btn = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
        # For alchemy lab
        alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
        alchemy_no = int(alchemy.text.split()[3].replace(",", ""))
        alchemy_btn = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
        # For portal
        portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
        portal_no = int(portal.text.split()[2].replace(",", ""))
        portal_btn = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
        # For time machine
        time_thing = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
        time_no = int(time_thing.text.split()[3].replace(",", ""))
        time_btn = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
        # get current cookie count
        number_text = driver.find_element(By.XPATH, '//*[@id="money"]').text
        if "," in number_text:
            number_text = number_text.replace(",", "")
        number = int(number_text)
        # For number
        if number <= 100:
            cursor_btn.click()
        elif number > 100 and number <= 500:
            grandma_btn.click()
        elif number > 500 and number <= 2000:
            mine_btn.click()
        elif number > 2000 and number <= 7000:
            shipment_btn.click()
        elif number > 7000 and number <= 50000:
            alchemy_btn.click()
        elif number > 50000 and number <= 1000000:
            portal_btn.click()
        elif number > 1000000 and number <= 123456789:
            time_btn.click()
        second = time.time() + 5
    if time.time() > timeout:
        cps = driver.find_element(By.XPATH, '//*[@id="cps"]').text
        print(cps)
        break





