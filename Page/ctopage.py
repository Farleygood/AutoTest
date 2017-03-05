# coding:utf-8
'''
Created on 2016年12月22日

@author: Administrator
'''

from selenium.webdriver.common.by import By
from elementmethod import WebUI
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time as t

class CtoPage(WebUI):
    
    click_login_loc = (By.XPATH,'//*[@id="login_status"]/a[1]')   # 进入登录页面
    click_username_loc = (By.XPATH,'//*[@id="loginform-username"]')   # 用户名输入框
    click_passwd_loc = (By.XPATH,'//*[@id="loginform-password"]')  # 密码框输入框
    click_loginbutton_loc = (By.XPATH,'//*[@id="login-form"]/div[3]/input')  # 登录提交按钮
    click_error_loc = (By.XPATH,".//*[@id='login-form']/div[2]/div/div")  # 登陆错误提示
    click_msg_loc = (By.XPATH,'//*[@id="login_status"]/div/a[2]')   # 消息
    click_blog_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/ul/li[1]/div[2]/a[2]')   # 博客按钮
    click_shequ_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/ul/li[1]/a')
    click_publishblog_loc = (By.XPATH,'/html/body/div[7]/div[2]/div[2]/div[1]/p/span[4]/a')   # 发布博客按钮
    click_publishtitle_loc = (By.XPATH,'//*[@id="isorg"]')   # 发表的标题下拉框
    click_publishtype_loc = (By.ID,'isorg')    # 发表的类型
    click_blogtitle_loc = (By.XPATH,'//*[@id="atc_title"]')   # blog标题
    click_blogcontent_loc = (By.XPATH,'/html/body')    # blog正文输入框
    click_bloglabel_loc = (By.XPATH,'//*[@id="tags"]')   #  博客标签
    click_systematics_loc = (By.XPATH,'//*[@id="classname"]')  # 博文分类
    click_selectsystematics_loc = (By.XPATH,'/html/body/div[13]/div[2]/div[2]/ul/li[8]/input')   # 选择分类
    click_confirmbutton_loc = (By.XPATH,'/html/body/div[13]/div[11]/div/button[1]') # 点击分类确认按钮
    click_submitbutton_loc = (By.XPATH,'//*[@id="tjj"]')   #点击提交按钮
    
    def getLoginButton(self):
        self.wait
        self.findElement(*self.click_login_loc).click()
        
    def getUserNameField(self,username):
        self.wait
        self.findElement(*self.click_username_loc).send_keys(username)
        
    def getPassWdField(self,passwd):
        self.wait
        self.findElement(*self.click_passwd_loc).send_keys(passwd)
        
    def getSubmitLogin(self):
        self.wait
        self.findElement(*self.click_loginbutton_loc).click()

    def getErrorMsg(self):
        self.wait
        return self.findElement(*self.click_error_loc).text
        
    def getMsgCount(self):
        self.wait
        print self.findElement(*self.click_msg_loc).text
        return self.findElement(*self.click_msg_loc).text

    # def click(self):
    #     self.wait
    #     self.findElement(*self.click_blog_loc).click()

    def getShequ(self):
        self.wait
        self.findElement(*self.click_shequ_loc).click()
        
    def getBlogButton(self):
        self.wait
        self.findElement(*self.click_blog_loc).click()
        
    def getPushblog(self):
        self.wait
        self.findElement(*self.click_publishblog_loc).click()
        
    def getPushTitle(self):
        self.wait
        self.findElement(*self.click_publishtitle_loc).click()
        
# 通过Select类选择发布的博文类型，通过id索引       
    def getPushType(self, ID):
        self.wait
        self.findElement(*self.click_publishtype_loc).click()
        select = Select(self.driver.find_element_by_id('isorg'))
        select.select_by_index(ID)

    def getBlogTitle(self,title):    
        self.wait
        self.findElement(*self.click_blogtitle_loc).send_keys(title)
        
    def getBlogContent(self,content):
        self.wait
        self.findElement(*self.click_blogcontent_loc).send_keys(content)
        
    def getBlogLabel(self,label):
        self.wait
        self.findElement(*self.click_bloglabel_loc).send_keys(label)
        
    def getSystematics(self):
        self.wait
        self.findElement(*self.click_systematics_loc).click()
        
    def getSelectSystematics(self):
        self.wait
        self.findElement(*self.click_selectsystematics_loc).click()
        
    def getConfirmBt(self):
        self.wait
        self.findElement(*self.click_confirmbutton_loc).click()
        
    def getSubmitPush(self):
        self.wait
        self.findElement(*self.click_submitbutton_loc).submit()
        
    def Login(self,username,passwd):
        self.doLogin(username,passwd)
    
    def doLogin(self,username,passwd):
        self.wait
        self.getUserNameField(username)
        self.getPassWdField(passwd)
        self.getSubmitLogin()

    def PublishBlog(self,ID,title,content,label):
        self.wait
        self.getShequ()
        nowHandurl = self.driver.current_window_handle
        self.getBlogButton()
        t.sleep(5)
        handles = self.driver.window_handles
        t.sleep(5)
        for handle in handles:
            if handle != nowHandurl:
                self.driver.switch_to.window(handle)
                t.sleep(5)
                self.getPushblog()
                nowHand_addblog = self.driver.current_window_handle
                t.sleep(3)
                handles = self.driver.window_handles
                t.sleep(5)
                for handle in handles:
                    if handle != nowHandurl and handle != nowHand_addblog:
                        self.driver.switch_to.window(handle)
                        t.sleep(3)
                        self.getPushType(ID)
                        self.getBlogTitle(title)
                        t.sleep(3)
                        self.driver.switch_to.frame('ueditor_0')
                        self.getBlogContent(content)
                        self.driver.switch_to.default_content()
                        self.getBlogLabel(label)
                        self.getSystematics()
                        self.getSelectSystematics()
                        self.getConfirmBt()
                        self.getSubmitPush()