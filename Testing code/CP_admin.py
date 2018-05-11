import unittest
from selenium import webdriver
import time


class RegisterTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()

        # Test success login
        self.username_val = "admin"
        self.password_val = "cp123456"

     
    def test_submission_success(self):
        driver = self.driver

        driver.get('http://couchpotatoes.pythonanywhere.com/admin/login/?next=/admin/')

        username = driver.find_element_by_id('id_username')
        username.send_keys(self.username_val)

        password = driver.find_element_by_id('id_password')
        password.send_keys(self.password_val)

        driver.find_element_by_xpath("//*[@id="login-form"]/div[3]/input").click()

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