from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

driver.find_element(By.ID,"shopping_cart_container").click()
driver.find_element(By.ID,"checkout").click()

driver.find_element(By.ID,"first-name").send_keys("Divyashree")
driver.find_element(By.ID,"postal-code").send_keys("572103")
driver.find_element(By.ID,"continue").click()
error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text

if error_message == "Error: Last Name is required":
   print("Error message verified successfully")
else:
    print("Error message verification failed")





