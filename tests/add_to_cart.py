from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for Products page
time.sleep(2)

# Add one product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Go to cart page
driver.find_element(By.ID, "shopping_cart_container").click()

# Verify cart quantity
quantity = driver.find_element(By.CLASS_NAME, "cart_quantity")
cart_count = quantity.text

if cart_count == "1":
    print("✅ Cart count is correct:", cart_count)
else:
    print("❌ Cart count is not correct")

# Close browser
driver.quit()
