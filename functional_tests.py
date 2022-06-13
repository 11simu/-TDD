from selenium import webdriver  
import unittest

class NewVisitorTest(unittest.TestCase):   #1

    def setUp(self):#3
        self.browser=webdriver.Firefox()

    def tearDown(self):#3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):#2


        self.browser.get('http://localhost:8000') 


        self.assertIn('To-Do',self.browser.title),"Browser title was:" + self.browser.title
        self.fail('Finish the test!')




if __name__=='__main__':#6
    unittest.main(warnings='ignore')#7
