from selenium import webdriver
from selenium.webdriver.common.by import By

def test_logout():
    driver=webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    login_message=driver.find_element(By.CLASS_NAME,"post-title").text
    assert "Logged In Successfully" in login_message
    print("loggin successfull")
    driver.quit()

