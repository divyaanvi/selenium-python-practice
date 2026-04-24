from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

products=driver.find_elements(By.CLASS_NAME,"inventory_item")
count=len(products)

print((type(products)))
\

print("Number of products:",count)

if count>0:
    print("products are listed in the website")
else:
    print("products are not listed")
