from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_invalid_password():

 driver = webdriver.Chrome()
 driver.get("https://practicetestautomation.com/practice-test-login/")    
 driver.find_element(By.ID,"username").send_keys("student")
 driver.find_element(By.ID,"password").send_keys("Password")
 driver.find_element(By.ID,"submit").click()
 time.sleep(5)
 errormessage=driver.find_element(By.ID,"error").text
 print(errormessage)
 assert "Your password is invalid!"in errormessage

 driver.quit()