from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# ✅ Correct locator and validation
page_title = driver.find_element(By.CLASS_NAME, "title").text

if page_title == "Products":
    print("✅ Page loaded successfully")
else:
    print("❌ Page not loaded")

driver.quit()