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
        time.sleep(10)

        print('Logo:')                                                                           #Logo
        Logo = driver.find_element_by_xpath(' // html/body/div[@class=\'comingsoonlogo\']/img[@src=\'/static/images/CouchPotatoesLogo.png\']')
        print('Logo is display Properly \n ')

        print('Title:')                                                                          #Title
        if ('TUBES' in driver.page_source):
            self.assertTrue ('TUBES' in driver.page_source)
            print('Title is display properly \n')
        else:
            print('Text is not present \n')
        time.sleep(10)

        #Description
        print('Description:')
        if ('Tubes is a connecting dots game. The game has network of squares and some of the squares contain dots.' in driver.page_source): 
            self.assertTrue ('Tubes is a connecting dots game. The game has network of squares and some of the squares contain dots.' in driver.page_source)
        else:
            print('fail')
        time.sleep(10)

        if ('There are exactly two alike dots which should relate to each other.' in driver.page_source): 
            self.assertTrue ('There are exactly two alike dots which should relate to each other.' in driver.page_source)
        else:
            print('fail')

        if ('To complete the game, all the matching dots must be connected.' in driver.page_source): 
            self.assertTrue ('To complete the game, all the matching dots must be connected.' in driver.page_source)
        else:
            print('fail')
        print('Description is display properly \n')
        time.sleep(10)

        print('Coming Soon Banner:')
        if ('Coming Soon' in driver.page_source):                                                #Coming Soon Banner
            self.assertTrue ('Coming Soon' in driver.page_source)
            print('Coming Soon banner is display properly \n')
        else:
            print('The displayed Coming Soon banner is not correct \n')
        
    def teardown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()