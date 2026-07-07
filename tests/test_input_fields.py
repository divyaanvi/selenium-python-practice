from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_input_fields():
    driver= webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID,"menu-primary-items").click()
    inputs=driver.find_elements(By.TAG_NAME,"input")
    print(len(inputs))
    for field in inputs:
        print(field.get_attribute("ID"))

    driver.quit()   

