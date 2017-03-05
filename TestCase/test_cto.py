# coding:utf-8
'''
Created on 2016年12月22日

@author: Administrator
'''

import unittest
from Page.basetestcase import BaseTestCase
from Page.ctopage import CtoPage
from model.log import logger
from ddt import ddt,data,unpack
from model.Model import DataHelper
import time

@ddt 
class ctoPageTest(BaseTestCase,CtoPage):
    
    @data((DataHelper().getXmlUser('login1', 'username'),
           DataHelper().getXmlUser('login1', 'passwd')))
    # @data(*Model.DataHelper().readExcels())
    @unpack
    def testLogin_001(self,username,passwd):
        '''测试51cto登录'''
        self.Login(username, passwd)
        time.sleep(5)
        self.assertEqual(u'消息(1)', self.getMsgCount())
        self.getMsgCount()
        logger.info('登录成功！')

    @data((DataHelper().getXmlUser('login2', 'username'),
           DataHelper().getXmlUser('login2', 'passwd')))
    # @data(*Model.DataHelper().readExcels())
    @unpack
    def testLogin_002(self,username,passwd):
        '''测试51cto登录'''
        self.Login(username, passwd)
        time.sleep(5)
        self.assertEqual(u'账号/密码错误', self.getErrorMsg())
        print self.getErrorMsg()
        logger.info('登录失败，账户/密码错误！')

if __name__ == '__main__':
    unittest.main(verbosity=2)

