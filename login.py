from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data,file_data,unpack
import unittest
from selenium.common.exceptions import NoSuchElementException
import math
import os

@ddt
class testing(unittest.TestCase):

    # dir = os.getcwd()
    # print dir
    def setUp(self):
        self.driver = webdriver.Chrome()

    @file_data("data/login.json")
    def test_login(self,data_set):
            driver = self.driver
            driver.get("http://ymail.com")
            #assert data_set['value'] in driver.title
            elem = driver.find_element_by_id("login-username")
            elem.send_keys(data_set['value'])
            elem.send_keys(Keys.RETURN)


            elem.send_keys(Keys.RETURN)
            elem2 = driver.find_element_by_id("login-signin")
            elem2.click()
            if driver.find_element_by_id("username-error"):
                print "Username doesnt exist"
            else :
                print "username found"
    def tearDown(self):
        self.driver.close()

    # @file_data('data.json')
    # def test_data(self, data_set):
    #     print data_set['start']

    # @file_data("data.json")
    # def test_dict(self, data_set):
    #     try:
    #         self.assertLess(data_set['start'],data_set['end'])
    #
    #     except AssertionError as e:
    #         print("Exception= '{0}'".format(e.message))
    #         raise

        # self.assertLess(data_set['value'], data_set['end'])
        # self.assertGreater(data_set['value'], data_set['end'])



    # @data(1, 2)
    # def test_greater_than_zero(self, value):
    #     self.assertGreater(value, 0)


    # def tearDown(self):
    #    self.close_browser('Login')
# @file_data('data.json')
# def login():
#     try:
#
#         driver = webdriver.Firefox()
#         driver.get("http://ymail.com")
#         assert "Yahoo" in driver.title
#         elem = driver.find_element_by_name("username")
#         elem.clear()

#         elem.send_keys(Keys.RETURN)
#     except:
#         assert "No results found." not in driver.page_source
#
#     driver.close()



if __name__ == '__main__':
    unittest.main()