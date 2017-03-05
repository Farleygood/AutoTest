# coding:utf-8
'''
Created on 2017年3月4日

@author: Administrator
'''

import unittest
from Page.basetestcase import BaseTestCase
from Page.ctopage import CtoPage
from model.log import logger
from ddt import ddt,data,unpack
from model.Model import DataHelper
import time as t

@ddt
class PublishBlog(BaseTestCase, CtoPage):

    @data((DataHelper().getXmlUser('publish1','ID'),
          DataHelper().getXmlUser('publish1','title'),
          DataHelper().getXmlUser('publish1','content'),
          DataHelper().getXmlUser('publish1','lable')),\
        (DataHelper().getXmlUser('publish2','ID'),
          DataHelper().getXmlUser('publish2','title'),
          DataHelper().getXmlUser('publish2','content'),
          DataHelper().getXmlUser('publish2','lable'))
        )
    @unpack
    def test_publish001(self,ID,title,content,lable):
        '''测试发布博客'''
        logger.info(u'正在登陆...')
        self.Login('619988077@qq.com', 'fanlei200491')
        logger.info(u'正在发布博客')
        self.PublishBlog(ID,title,content,lable)
        # t.sleep(20)
        self.assertEqual('http://blog.51cto.com/user_index.php?action=addblog_new', self.driver.current_url)
        logger.info(u'博客发布成功')

    # @data((DataHelper().getXmlUser('publish1','ID')),
    #       (DataHelper().getXmlUser('publish1','title')),
    #       (DataHelper().getXmlUser('publish1','content')),
    #       (DataHelper().getXmlUser('publish1','lable')))
    # @unpack
    #
    # def test_publish002(self,ID,title,content,lable):
    #
    #     logger.info(u'正在登陆...')
    #     self.Login('619988077@qq.com', 'fanlei200491')
    #     logger.info(u'正在发布第二篇博客')
    #     self.PublishBlog(ID,title,content,lable)
    #     t.sleep(5)
    #     self.assertEqual('', self.driver.current_url)
    #     logger.info(u'第二篇博客发布成功')

if __name__ == '__main__':
    unittest.main(verbosity=2)

