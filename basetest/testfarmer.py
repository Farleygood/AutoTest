# coding:utf-8
'''
Created on 2016年12月27日

@author: Administrator
'''

from selenium import webdriver
from Page.ctopage import CtoPage
from model.log import logger
import time as t
import unittest


class ctopage(unittest.TestCase):
     
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.51cto.com/")
        
    def test_001(self): 
        u'''测试51cto title是否正确'''
        logger.info(u'执行test__001')
        self.assertEqual(u'51CTO.COM - 技术成就梦想 - 中国领先的IT技术网站', self.driver.title)
        
    def test_002(self): 
        u'''测试51cto 网址是否正确'''
        logger.info(u'执行test__002')
        self.assertEqual(u'http://www.51cto.com/', self.driver.current_url)
    
    logger.info(u'跳过用例test__003')
    # @unittest.skip('this case skip')
    def test_003(self):        
        u'''测试跳转到登录页面是否成功'''
        logger.info(u'执行test__003')
        t.sleep(3)
        CtoPage(self.driver).getLoginButton()
        t.sleep(3)
        self.assertEqual(u'http://home.51cto.com/index?reback=http://www.51cto.com/', self.driver.current_url)
          
    
          
    def tearDown(self):
        self.driver.quit()
        
    @staticmethod
    def suite():
        # 使用TestLoader()
#         suite = unittest.TestLoader.loadTestsFromTestCase(ctopage)
        suite = unittest.TestSuite(unittest.makeSuite(ctopage))
        return suite
         
if __name__ == '__main__':
    
    # 1. addTest方法
#     suit = unittest.TestSuite()
#     suit.addTest(ctopage('test_001'))
#     suit.addTest(ctopage('test_002'))
#     suit.addTest(ctopage('test_003'))

    # 2. 优化代码，使用makeSuit方法,只用传入测试类名即可
#     suit = unittest.TestSuite(unittest.makeSuite(ctopage))
#     unittest.TextTestRunner(verbosity=2).run(suit)
    
    # 3. 再次优化，使用静态方法
    unittest.TextTestRunner(verbosity=2).run(ctopage.suite())
    
#     unittest.main(verbosity=2)

