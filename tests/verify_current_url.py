from selenium import webdriver
from selenium.webdriver.common.by import By

def verify_url():
    driver=webdriver.Chrome()
    driver.get("https://practicetestautomation.com/")
    driver.get("https://practicetestautomation.com/practice-test-login/")    
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    current_url= driver.current_url
    assert "https://practicetestautomation.com/logged-in-successfully/" in current_url
    print("url verified succesfully")
    driver.quit