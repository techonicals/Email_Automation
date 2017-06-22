from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data,file_data,unpack
import unittest
import math

@ddt
class testing(unittest.TestCase):
    @file_data('data.json')
    def test_data(self, data_set):
        print data_set['start']

        # start = data_set['start']
        # print start



    # @data(1, 2)
    # def test_greater_than_zero(self, value):
    #     self.assertGreater(value, 0)


# @file_data('data.json')
# def login():
#     try:
#
#         driver = webdriver.Firefox()
#         driver.get("http://ymail.com")
#         assert "Yahoo" in driver.title
#         elem = driver.find_element_by_name("username")
#         elem.clear()
#         elem.send_keys.get('data','use')
#         elem.send_keys(Keys.RETURN)
#     except:
#         assert "No results found." not in driver.page_source
#
#     driver.close()



if __name__ == '__main__':
    unittest.main()