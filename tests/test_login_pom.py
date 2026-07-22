from pages.login_page import LoginPage

def test_login(driver):

    driver.get("https://practicetestautomation.com/practice-test-login/")

    page = LoginPage(driver)

    page.enter_username("student")
    page.enter_password("Password123")
    page.click_submit()
    page.login("student","wrongpassword")
    

    heading = page.get_heading()

    assert heading == "Logged In Successfully"

