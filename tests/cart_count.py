from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# add product first
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# get quantity
quantity = driver.find_element(By.CLASS_NAME, "cart_quantity").text

print(quantity)

driver.quit()