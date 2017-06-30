from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data,file_data,unpack
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.action_chains import ActionChains
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
                username = driver.find_element_by_id("login-username")
            elif mail == 'http://gmail.com':
                username = driver.find_element_by_id("identifierId")
            else:
                username = driver.find_element_by_id("login-username")
            username.send_keys(data_set['value'])
            username.send_keys(Keys.RETURN)
            driver.implicitly_wait(3)
            driver.find_element_by_name("password").send_keys(data_set['pass'])
            #password.send_keys(data_set['pass'])
            signin = driver.find_element_by_id("login-signin")
            signin.click()
            #driver.implicitly_wait(3)
            inbox = driver.find_element_by_xpath(".//*[@class ='listnav-outter']")
            if inbox.is_enabled():
                print "logged in"
            hover_un = driver.find_element_by_xpath(".//*[@id='uhWrapper']/table/tbody/tr/td[3]/ul/li[2]/a/b [contains(@title,'Hi')]")
            hover = ActionChains(driver).move_to_element(hover_un)
            hover.click().perform()
            # driver.implicitly_wait(3)
            driver.find_element_by_xpath(".//*[(@id='yucs-signout') and contains(@href,'https://login.yahoo.com') ]").click()
            logo = driver.find_element_by_id("uh-logo")
            if logo.is_displayed():
                print "logged out"
            # unError = driver.find_element_by_id("username-error")
            #
            # if unError.is_enabled():
            #     print "Username doesnot Exist"
            # else :
            #     print "Username Exists"

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()