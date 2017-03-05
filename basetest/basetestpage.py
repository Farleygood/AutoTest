# coding:utf-8
'''
Created on 2016年12月21日

@author: Administrator
'''
__version__ = '0.1.0'

from selenium import webdriver
import time
from Page.elementmethod import WebUI
from Page.ctopage import CtoPage 
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def sleeptime(sltime):
    time.sleep(sltime)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.51cto.com')
driver.find_element_by_xpath('//*[@id="login_status"]/a[1]').click()
# CtoPage(driver).click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="loginform-username"]').send_keys('619988077@qq.com')
sleeptime(2)
driver.find_element_by_xpath('//*[@id="loginform-password"]').send_keys('xxxxxx')
sleeptime(2)
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
sleeptime(5)
msg = driver.find_element_by_xpath('//*[@id="login_status"]/div/a[2]').text
print '未读消息数：',msg[3],u'条'
nowHandurl = driver.current_window_handle
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/li[1]/a').click()

driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/li[1]/div[2]/a[2]').click()  #点击博客
time.sleep(5)
handles = driver.window_handles  # 获取当前浏览器的所有窗口
for handle in handles:
    if handle != nowHandurl:
        driver.switch_to.window(handle)
        print u'我跳转到了发表博客页面,url:', driver.current_url
        time.sleep(8)
        driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/p/span[4]/a').click() # 点击发表博文
        time.sleep(5)
        nowHand_addblog = driver.current_window_handle
        handles = driver.window_handles  # 获取当前浏览器的所有窗口
        time.sleep(5)
        for handle in handles:
            if handle != nowHandurl and handle != nowHand_addblog:
                driver.switch_to.window(handle)
                print u'我跳转到了管理后台，发布博客,url:', driver.current_url
                driver.find_element_by_xpath('//*[@id="isorg"]').click()
                select = Select(driver.find_element_by_id('isorg'))
                select.select_by_index(2)
                driver.find_element_by_xpath('//*[@id="atc_title"]').send_keys(u'发布博文标题')
                sleeptime(3)
                driver.switch_to.frame('ueditor_0')  # 切换到正文输入框的frame
                driver.find_element_by_xpath('/html/body').send_keys(u'这是发布博文正文\r\n这是第二行\r\n这是第三行\r\n###########')
                driver.switch_to.default_content()  # 从frame中切回主文档
                driver.find_element_by_xpath('//*[@id="tags"]').send_keys(u'博文标签')
                driver.find_element_by_xpath('//*[@id="classname"]').click()
                driver.find_element_by_xpath('/html/body/div[13]/div[2]/div[2]/ul/li[8]/input').click()
                driver.find_element_by_xpath('/html/body/div[13]/div[11]/div/button[1]').click()
                driver.find_element_by_xpath('//*[@id="tjj"]').submit()
                sleeptime(3)
                assert 'http://blog.51cto.com/user_index.php?action=addblog_new' == driver.current_url
                print u'博客发布成功...'

sleeptime(5)                
driver.quit()



