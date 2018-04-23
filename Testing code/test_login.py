import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class RegisterTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome('/Users/kishore/Downloads/chromedriver')

    def test_submission(self):
        driver = self.driver

        username_val = "test1234"
        email_val = "test1@test.com"
        password_val = "TheDevilInI"

        driver.get('http://127.0.0.1:8000/register/')

        username = driver.find_element_by_id('id_username')
        username.send_keys(username_val)

        email = driver.find_element_by_id('id_email')
        email.send_keys(email_val)

        password = driver.find_element_by_id('id_password1')
        password.send_keys(password_val)

        confirmpassword = driver.find_element_by_id('id_password2')
        confirmpassword.send_keys(password_val)

        driver.find_element_by_xpath("//input[@type='submit' and @value='Register']").click()

        if ('Welcome to Couch Potatoes Gaming Community' in driver.page_source):

            print("Page is in login")

            login_username = driver.find_element_by_id('id_username')
            login_username.send_keys(username_val)

            login_password = driver.find_element_by_id('id_password')
            login_password.send_keys(password_val)

            driver.find_element_by_xpath("//button[@type='submit']").click()

            if ('TUBES' in driver.page_source):
                print("Logged into the page")

        time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()