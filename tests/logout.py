from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

title=driver.find_element(By.CLASS_NAME,"title").text

if title== "Products":
    print("page title verified successfully")
else:
    print("verification failed")

driver.find_element(By.ID,"react-burger-menu-btn").click()
driver.find_element(By.ID,"logout_sidebar_link").click()

driver.quit()