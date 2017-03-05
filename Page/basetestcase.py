# coding:utf-8
'''
Created on 2016年12月22日

@author: Administrator
'''

from selenium import webdriver
import unittest

class BaseTestCase(unittest.TestCase):
        
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://home.51cto.com/index?reback=http://www.51cto.com/')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
