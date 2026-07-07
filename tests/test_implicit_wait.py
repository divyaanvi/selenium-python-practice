from selenium import webdriver
from selenium.webdriver.common.by import By

def test_implicit_wait():

    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    heading = driver.find_element(By.CLASS_NAME, "post-title").text

    assert "Logged In Successfully" in heading

    print("Login successful using implicit wait")

    driver.quit()