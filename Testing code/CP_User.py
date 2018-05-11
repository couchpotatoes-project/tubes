import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Tubes(unittest.TestCase):
    def setUp(self):
        
        #self.driver = webdriver.Ie()
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
    def test_submission(self):      
        driver = self.driver   

        driver.get('http://couchpotatoes.pythonanywhere.com/')
        self.assertIn('Tubes',driver.title)        
        time.sleep(7)

        #Code is commented as user is already registered for Tubes.
        '''        
        Signup = driver.find_element_by_partial_link_text('Sign Up')
        Signup.click()
        time.sleep(3)

        text_input_vals = {
            'username' : 'siddhi117',                                                             
            'email' : 'sshah33@kent.edu',
            'password1' : 'admin123',
            'password2' : 'admin123',

        }

        for name, text in text_input_vals.items():
            text_input_elem = driver.find_element_by_name(name)
            text_input_elem.send_keys(text) 
        time.sleep(3)

        register = driver.find_element_by_id('RegisterButton')
        register.click()
        time.sleep(10)

        home_page = driver.find_element_by_xpath(' //html/body/div[@class=\'container-fluid\']/div[@class=\'row\']/div[@class=\'col-sm-2\']/a/img[@src=\'/static/images/CouchPotatoesLogo.png\']')
        home_page.click()
        time.sleep(3)'''
        
        #Rules Link
        rules = driver.find_element_by_partial_link_text('Rules')
        rules.click()
        time.sleep(3)

        #Scroll Down
        driver.execute_script("window.scrollTo(0, 200);")
        time.sleep(3)

        #Next aero
        next_button1 = driver.find_element_by_class_name('next')
        next_button1.click()
        time.sleep(2)

        next_button2 = driver.find_element_by_class_name('next')
        next_button2.click()
        time.sleep(2)

        next_button3 = driver.find_element_by_class_name('next')
        next_button3.click()
        time.sleep(2)

        next_button4 = driver.find_element_by_class_name('next')
        next_button4.click()
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        #video = driver.find_element_by_xpath(' // html/body/div[@class=\'container-fluid\']/div[@class=\'container\']/div[@class=\'video\']/video[@src=\'/static/videos/demo.mp4\']')
        #print('Video is display Properly \n ')
        #video.click()
        #time.sleep(3)

        #Click on Play Button
        play_button = driver.find_element_by_id('PlayButton')
        play_button.click()
        time.sleep(3)
        
        #Login Page : Credentials 
        text_input_vals = {
            'username' : 'siddhi117',                                                             
            'password' : 'admin1234',
        }

        for name, text in text_input_vals.items():
            text_input_elem = driver.find_element_by_name(name)
            text_input_elem.send_keys(text) 
        time.sleep(5)

        #Login Button
        login_button = driver.find_element_by_id('LoginButton')
        login_button.click()
        time.sleep(4)
        
                
    def teardown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()