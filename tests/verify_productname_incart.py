from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

if product_name == "Sauce Labs Bike Light":
    print("Name verified successfully")
else:
    print("Product name is incorrect")

driver.quit()