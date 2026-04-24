from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

time.sleep(2)   # ✅ wait for products page

items_list = driver.find_elements(By.CLASS_NAME,"inventory_item_price")  # ✅ fixed class name

for items in items_list:
    if items.text.startswith("$"):
        print("correct price format:")
    else:
        print("incorrect price format:")

driver.quit()