from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_success_msg():
    driver=webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    success_msg=driver.find_element(By.CLASS_NAME,"has-text-align-center").text
    assert "Congratulations student. You successfully logged in!" in success_msg

    print("successfull verification")