# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep


class HttpAgentStep2Page(Page):
    '''
    Http代理：配置详情
    '''
    url = '/ingress/createPage/step2?domainId=&serviceId=1979'

    # define the Http item{
    domain_name = (By.ID,"domain")                                          # 域名
    visit_path = (By.ID,"visitPath")                                       # 访问路径
    service_port = (By.ID, "servicePort")                                  # 端口
    location_config_state = (By.ID, "locationConfig_state")               # 配置复选框
    location_config_state_button = (By.ID, "locationConfig_state_btn")   # 配置展开按钮
    affinity = (By.ID, "affinity")                                          # 配置cookie
    session_cookie_name = (By.ID, "sessionCookieName")                    # cookie名
    session_cookie_hash = (By.ID, "sessionCookieHash")                    # 散列算法
    create_button = (By.ID, "createButton")                                # 创建按钮
    laststep_button = (By.LINK_TEXT, "上一步")                              # 上一步按钮

    # 输入创建的域名
    def write_domain_name(self):
        self.find_element(*self.domain_name).click()
        self.find_element(*self.domain_name).send_keys("test.auto.bcm")

    # 输入访问路径
    def write_visit_path(self):
        self.find_element(*self.visit_path).click()
        self.find_element(*self.visit_path).send_keys("versionone")

    # 输入端口号
    def write_service_port(self):
        self.find_element(*self.service_port).click()
        self.find_element(*self.service_port).send_keys("8080")

    # 复选框
    def click_location_config_state(self):
        self.find_element(*self.location_config_state).click()

    # 展开按钮
    def click_location_config_state_button(self):
        self.find_element(*self.location_config_state_button).click()

    # 配置cookie
    def write_affinity(self):
        self.find_element(*self.affinity).click()
        self.find_element(*self.affinity).send_keys("cookie")

    # 配置cookie名
    def write_cookie_name(self):
        self.find_element(*self.session_cookie_name).click()
        self.find_element(*self.session_cookie_name).send_keys("cookiename")

    # 配置cookie使用的散列算法
    def write_cookie_hash(self):
        self.find_element(*self.session_cookie_hash).click()
        self.find_element(*self.session_cookie_hash).send_keys("md5")

    # 上一步按钮
    def click_last_button(self):
        self.find_element(*self.laststep_button).click()

    # 创建按钮
    def click_create_button(self):
        self.find_element(*self.create_button).click()

# }define the Http item

# define the Http action{

# }define the Http action

