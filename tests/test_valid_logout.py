from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def valid_logout():
    driver=webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")    
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    driver.find_element(By.CLASS_NAME,"Log out").click()
    print("logged out successfuly")
    driver.quit()