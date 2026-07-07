from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_page():

    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    submit = driver.find_element(By.ID, "submit")

    assert username.is_enabled()
    assert username.is_displayed()

    assert password.is_enabled()
    assert password.is_displayed()

    assert submit.is_enabled()
    assert submit.is_displayed()

    print("All login page elements verified successfully")

    driver.quit()
