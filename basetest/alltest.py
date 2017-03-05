# coding:utf-8
'''
Created on 2016年12月27日

@author: Administrator
'''

import  unittest,sys,HTMLTestRunner,time
reload(sys)
# sys.setdefaultencoding('utf-8')
from model.log import logger


def suite():
    logger.info('this is run suite')
    dir_case=unittest.defaultTestLoader.discover(
        'D:/Eclipseworkspace/AutoTest/src/basetest/',
        pattern='testfarmer.py',
        top_level_dir=None
    )
    logger.info('this is run suite done')
    return dir_case

#获取当前时间另外一种方式是:
#nowTime=time.strftime('%Y-%m-%d %X',time.localtime())

def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))


def runAutomation():

    filename='D:/Eclipseworkspace/AutoTest/src/Report/'+getNowTime()+'TestReport.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'自动化测试报告详细的信息'
    )
    runner.run(suite())

if __name__=='__main__':
    runAutomation()
    