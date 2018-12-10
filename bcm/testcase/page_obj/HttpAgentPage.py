# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login
from time import sleep


class HttpAgentPage(Page):
    '''
    Http代理列表页
    '''
    url = '/ingress'

    # define the Http item{

    http_agent_create = (By.ID, "ingressCreateBtn")                                                                     # 创建
    http_agent_reload = (By.ID, "ingressReloadBtn")                                                                     # 刷新
    http_agent_search = (By.XPATH, '/html/body/div[3]/article/div/div[3]/div/div[1]/div[2]/div/label/input')   # 搜索
    http_agent_edit = (By.XPATH, "/html/body/div[3]/article/div/div[3]/div/table/tbody/tr[1]/td[3]/a[1]/i")    # 编辑
    http_agent_delete = (By.ID, "deleteTcpService")                                                                     # 删除
    http_agent_delete_confirm = (By.LINK_TEXT,"确认")                                                                     # 确认删除
    http_agent_delete_cancel = (By.LINK_TEXT, "取消")                                                                     # 取消删除

    # 创建按钮
    def create_button(self):
        self.find_element(*self.http_agent_create).click()

    # 刷新按钮
    def reload_button(self):
        self.find_element(*self.http_agent_reload).click()

    # 搜索按钮
    def search_button(self,domain_name):
        self.find_element(*self.http_agent_search).click()
        self.find_element(*self.http_agent_search).send_keys(domain_name)

    # 编辑按钮
    def edit_button(self):
        self.find_element(*self.http_agent_edit).click()

    # 删除按钮
    def delete_button(self):
        self.find_element(*self.http_agent_delete).click()
        self.find_element(*self.http_agent_delete_confirm).click()    # 确认删除
        self.find_element(*self.http_agent_delete_cancel).click()     # 取消删除

    # 登录到http
    def lonin_http_page(self):
        Login(self.driver).user_login()
        Page.open(self)
# }define the Http item

# define the Http action{

# }define the Http action

