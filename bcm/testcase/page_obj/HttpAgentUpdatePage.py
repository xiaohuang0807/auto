# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep

class HttpAgentUpdatePage(Page):
    '''
    Http代理：修改配置
    '''
    url = '/ingress/updateIngressPage?domain=test.dockerfiletest'

    # define the Http item{
    visit_path = (By.ID,"visitPath00")                                       # 访问路径
    service_port = (By.ID, "servicePort00")                                  # 端口
    location_config_state = (By.ID, "locationConfig_state0")                # 配置复选框
    location_config_state_button = (By.ID, "locationConfig_state0_btn")    # 配置展开按钮
    affinity = (By.ID, "affinity0")                                           # 配置cookie
    session_cookie_name = (By.ID, "sessionCookieName0")                     # cookie名
    session_cookie_hash = (By.ID, "sessionCookieHash0")                     # 散列算法
    create_button = (By.ID, "updateLocationButton0")                        # 修改按钮
    delete_button = (By.XPATH,"/html/body/div[3]/article/div/div[3]/form/ul/li/div[2]/div/ul/li[4]/span[1]/button")    # 删除
    delete_confirm = (By.LINK_TEXT,"确认")                                     # 确认删除
    delete_cancel = (By.LINK_TEXT, "取消")                                     # 取消删除

    # 修改访问路径
    def update_visit_path(self,visitpath):
        self.find_element(*self.visit_path).click()
        self.find_element(*self.visit_path).send_keys(visitpath)

    # 修改端口号
    def update_visit_path(self,port):
        self.find_element(*self.service_port).click()
        self.find_element(*self.service_port).send_keys(port)

    # 复选框
    def click_location_config_state(self):
        self.find_element(*self.location_config_state).click()

    # 展开按钮
    def click_location_config_state_button(self):
        self.find_element(*self.location_config_state_button).click()

    # 修改cookie
    def update_affinity(self,cookie):
        self.find_element(*self.affinity).click()
        self.find_element(*self.affinity).send_keys(cookie)

    # 修改cookie名
    def update_cookie_name(self):
        self.find_element(*self.session_cookie_name).click()
        self.find_element(*self.session_cookie_name).send_keys("newname")

    # 修改cookie使用的散列算法
    def update_cookie_hash(self):
        self.find_element(*self.session_cookie_hash).click()
        self.find_element(*self.session_cookie_hash).send_keys("md5")

    # 修改按钮
    def update_create_button(self):
        self.find_element(*self.create_button).click()

    # 删除按钮
    def delete_config(self):
        self.find_element(*self.delete_button).click()
        self.find_element(*self.delete_confirm).click()    # 确认删除
        self.find_element(*self.delete_cancel).click()     # 取消删除


# }define the Http item

# define the Http action{

# }define the Http action