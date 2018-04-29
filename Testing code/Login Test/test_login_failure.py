import unittest
from selenium import webdriver
import time


class RegisterTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome('/Users/kiran/Downloads/chromedriver')

        # Test validation failure
        self.username_val_success = "test1234test"
        self.email_val_success = "test@test.com"
        self.password_val_success = "TheDevilInI"

        self.username_val_fail = "test"
        self.email_val_fail = "testtest.com"
        self.password_val_fail = ""

    def test_validation_failure(self):
        driver = self.driver

        print("Test validation")

        driver.get('http://127.0.0.1:8000/register/')

        print("Check Email Validation")
        username = driver.find_element_by_id('id_username')
        username.send_keys(self.username_val_success)

        email = driver.find_element_by_id('id_email')
        email.send_keys(self.email_val_fail)

        password = driver.find_element_by_id('id_password1')
        password.send_keys(self.password_val_success)

        confirmpassword = driver.find_element_by_id('id_password2')
        confirmpassword.send_keys(self.password_val_success)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Register']").click()

        self.assertTrue("Enter a valid email address" in driver.page_source)

        time.sleep(10)

        print("Check UserName Validation")

        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username_val_fail)

        email = driver.find_element_by_id('id_email')
        email.clear()
        email.send_keys(self.email_val_success)

        password = driver.find_element_by_id('id_password1')
        password.clear()
        password.send_keys(self.password_val_success)

        confirmpassword = driver.find_element_by_id('id_password2')
        confirmpassword.clear()
        confirmpassword.send_keys(self.password_val_success)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Register']").click()

        self.assertTrue("Please enter valid values" in driver.page_source)

        time.sleep(10)

        print("Check Password Validation")

        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys(self.username_val_success)

        email = driver.find_element_by_id('id_email')
        email.clear()
        email.send_keys(self.email_val_success)

        password = driver.find_element_by_id('id_password1')
        password.clear()
        password.send_keys(self.password_val_fail)

        confirmpassword = driver.find_element_by_id('id_password2')
        confirmpassword.clear()
        confirmpassword.send_keys(self.password_val_fail)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Register']").click()

        self.assertTrue("Please enter valid values" in driver.page_source)

        time.sleep(10)

    def test_login_failure(self):
        driver = self.driver

        print("Test validation")

        driver.get('http://127.0.0.1:8000/login/')

        print("Check Login")
        username = driver.find_element_by_id('id_username')
        username.send_keys(self.username_val_success)

        password = driver.find_element_by_id('id_password')
        password.send_keys(self.password_val_success)

        driver.find_element_by_css_selector(".btn.btn-primary").click()

        self.assertTrue("Your username and password didn't match. Please try again." in driver.page_source)

        time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
