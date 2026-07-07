from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_explicit_wait():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "post-title"))
    ).text

    assert "Logged In Successfully" in heading

    print("Heading verified")

    driver.quit()