from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data,file_data,unpack
import unittest
from selenium.common.exceptions import NoSuchElementException
import math
import os

@ddt
class testing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    @file_data("data/login.json")
    def test_login(self,data_set):
            driver = self.driver
            mail = data_set['mail_app']
            driver.get(mail)
            #assert data_set['value'] in driver.title
            if mail == 'http://ymail.com':
                elem = driver.find_element_by_id("login-username")
            elif mail == 'http://gmail.com':
                elem = driver.find_element_by_id("identifierId")
            else:

                elem = driver.find_element_by_id("login-username")
            elem.send_keys(data_set['value'])
            elem.send_keys(Keys.RETURN)
            #elem2 = driver.find_element_by_id("login-signin")
            #elem2.click()
            elem4 = driver.find_element_by_id("username-error")
            if elem4.is_enabled():
                print "Username doesnot Exist"
            else :
                print "Username Exists"

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()