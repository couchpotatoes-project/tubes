import unittest
from selenium import webdriver
import time
from django.test import Client


class RegisterTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome('/Users/kiran/Downloads/chromedriver')

        self.username_val_success = "admin"
        self.password_val_success = "cp123456"

        self.username_val_failure = "mudmin"
        self.password_val_failure = "noooo"



    def test_login_failure(self):
        driver = self.driver

        print("Test Failure Login")

        driver.get('http://couchpotatoes.pythonanywhere.com/login/')

        username = driver.find_element_by_id('id_username')
        username.send_keys(self.username_val_failure)

        password = driver.find_element_by_id('id_password')
        password.send_keys(self.password_val_failure)

        time.sleep(5)

        driver.find_element_by_css_selector(".btn.btn-primary").click()

        self.assertTrue(
            "Your username and password didn't match. Please try again." in driver.page_source)

        time.sleep(10)

    def test_login_success(self):
        driver = self.driver

        print("Test Successful Login")

        driver.get('http://couchpotatoes.pythonanywhere.com/login/')

        username = driver.find_element_by_id('id_username')
        username.send_keys(self.username_val_success)

        password = driver.find_element_by_id('id_password')
        password.send_keys(self.password_val_success)

        time.sleep(5)

        driver.find_element_by_css_selector(".btn.btn-primary").click()

        self.assertTrue(
            "Level: " in driver.page_source)

        time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

