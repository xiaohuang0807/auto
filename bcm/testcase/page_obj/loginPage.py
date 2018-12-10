# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep


class Login(Page):
    '''
    用户登录页面
    '''
    url = '/login'

    # define the login item{

    login_username_loc = (By.ID, "userName")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.ID, "btn-signin")
    login_error_hint_loc = (By.XPATH, "/html/body/div/div/div/div[2]/div[1]/span")
    user_login_success_loc = (By.XPATH, "/html/body/header/div/div/ul/li/a")

    # 用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 用户密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()


# }define the login item

# define the login action{

    # 用户登录
    def user_login(self, username="zhengyin", password="zhengyin1234"):
        '''获取的用户名密码，并且登录'''
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)

    # 获取登录错误信息
    def get_login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text

    # 获取登录信息，验证成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

# }define the login action

