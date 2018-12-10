# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep


class HttpAgentStep1Page(Page):
    '''
    Http代理：创建域名，选择服务
    '''
    url = '/ingress/createPage/step1'

    # define the Http item{

    domain_name = (By.ID, "domainId")                                                                                                   # 域名
    domain_name_list = (By.XPATH,"/html/body/div[3]/article/div/div[3]/form/div/ul/li/div/div/ul/li[1]/select/option[2]")  # 域名列表 可变
    service_name = (By.ID, "serviceId")                                                                                                 # 服务名称
    service_name_list = (By.XPATH,"/html/body/div[3]/article/div/div[3]/form/div/ul/li/div/div/ul/li[2]/select/option[2]") # 服务列表 可变
    nextstep_button = (By.ID, "createButtonStep1")                                                                                    # 下一步按钮

    # 域名
    def write_domain_name(self):
        self.find_element(*self.domain_name).click()
        self.find_element(*self.domain_name_list).click()

    # 服务名称
    def write_service_name(self):
        self.find_element(*self.service_name).click()
        self.find_element(*self.service_name_list).click()

    # 下一步按钮
    def click_next_button(self):
        self.find_element(*self.nextstep_button).click()
# }define the Http item

# define the Http action{

# }define the Http action

