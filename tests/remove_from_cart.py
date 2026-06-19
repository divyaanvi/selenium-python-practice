from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

driver.find_element(By.ID, "shopping_cart_container").click()

driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
items = driver.find_elements(By.CLASS_NAME, "cart_item")

if len(items) == 0:
    print("Product removed successfully")
else:
    print("Product still exists in cart")

driver.quit()