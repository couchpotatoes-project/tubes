import unittest
from selenium import webdriver
import time


class RegisterTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome('/Users/kiran/Downloads/chromedriver')

        # Test success login
        self.username_val = "test1234"
        self.email_val = "test1@test.com"
        self.password_val = "TheDevilInI"

        # Test validation failure
        self.username_val_fail = "test1234test"
        self.email_val_fail = "testtest.com"
        self.password_val_fail = "TheDevilInI"

    def test_submission_success(self):
        driver = self.driver

        driver.get('http://127.0.0.1:8000/register/')

        username = driver.find_element_by_id('id_username')
        username.send_keys(self.username_val)

        email = driver.find_element_by_id('id_email')
        email.send_keys(self.email_val)

        password = driver.find_element_by_id('id_password1')
        password.send_keys(self.password_val)

        confirmpassword = driver.find_element_by_id('id_password2')
        confirmpassword.send_keys(self.password_val)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Register']").click()

        if ('Welcome to Couch Potatoes Gaming Community' in driver.page_source):

            print("Page is in login")

            login_username = driver.find_element_by_id('id_username')
            login_username.send_keys(self.username_val)

            login_password = driver.find_element_by_id('id_password')
            login_password.send_keys(self.password_val)

            driver.find_element_by_xpath("//button[@type='submit']").click()

            self.assertTrue('TUBES' in driver.page_source)
            print("Logged into the page")
        else:
            print("Login Failed")

        time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
