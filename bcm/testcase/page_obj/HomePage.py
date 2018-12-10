# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from bcm.testcase.page_obj.loginPage import Login
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep


class Navigation(Page):
    '''
    主页导航栏
    '''
    url = '/bcm/178'

    service_integration_loc = (By.XPATH, "/html/body/div[1]/div[2]/nav/div/ul/li[2]/a")            # 获取服务集成控件
    service_manage_loc = (By.XPATH, "/html/body/div[1]/div[2]/nav/div/ul/li[2]/ul/li[1]/a")                 # 获取服务管理控件
    xpath_service_manage = (By.XPATH, '//*[@id="li_service"]/a')    # 通过Xpath路径定位服务管理
    http_agent_loc = (By.LINK_TEXT, "HTTP代理")                     # 获取HTTP代理控件
    tcp_udp_agent_loc = (By.LINK_TEXT, "TCP/UDP代理")               # 获取TCP/UDP代理控件
    network_isolation_loc = (By.LINK_TEXT, "网络隔离")              # 获取网络隔离控件
    deamon_service_loc = (By.LINK_TEXT, "守护服务")                 # 获取守护服务控件
    introduce_external_services_loc = (By.LINK_TEXT, "引入外部服务") # 获取引入外部服务控件
    expansion_strategy_loc = (By.LINK_TEXT, "伸缩策略")             # 获取伸缩策略控件
    timed_task_loc = (By.LINK_TEXT, "定时任务")                     # 获取定时任务控件

    # 点击服务集成
    def click_service_integration(self):
        self.find_element(*Navigation.service_integration_loc).click()

    # 点击服务管理
    def click_service_manage(self):
        self.find_element(*Navigation.service_manage_loc).click()

    def into_home_page(self):
        Login(self.driver).user_login()

