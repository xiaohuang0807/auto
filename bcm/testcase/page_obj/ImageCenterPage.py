# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.ServiceManagePage import ServiceMange
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login


class ImageCenter(Page):
    '''
    镜像中心界面
    '''
    url = '/registry/0'

    deploy_image_loc = (By.XPATH, '//*[@id="imageList"]/tr[1]/td[9]/a[1]/i')    # 获取部署镜像按钮
    export_image_loc = (By.XPATH, '//*[@id="imageList"]/tr[1]/td[9]/a[2]/i')     # 获取导出镜像按钮
    collect_image_loc = (By.XPATH, '//*[@id="imageList"]/tr[1]/td[9]/a[3]/i')    # 获取收藏镜像按钮
    refresh_imagepage_loc = (By.ID, "volReloadBtn")   # 获取刷新页面按钮
    find_input_loc = (By.XPATH, '//*[@id="DataTables_Table_0_filter"]/label/input')  # 获取查找输入框
    all_checkbox_loc = (By.ID, "checkallbox")         # 获取所有复选框按钮
    image_checkbox_loc = (By.NAME, "ids")             # 获取镜像复选框按钮

    # 部署镜像
    def deploy_image(self):
        self.find_element(*ImageCenter.deploy_image_loc).click()

    # 导出镜像
    def export_image(self):
        self.find_element(*ImageCenter.export_image_loc).click()

    # 收藏镜像
    def collect_image(self):
        self.find_element(*ImageCenter.collect_image_loc).click()

    # 刷新页面
    def refresh_image_page(self):
        self.find_element(*ImageCenter.refresh_imagepage_loc).click()

    # 查找输入框
    def find_input(self):
        self.find_element(*ImageCenter.find_input_loc).click()

    # 选择所有复选框
    def check_all_checkbox(self):
        self.find_element(*ImageCenter.all_checkbox_loc).click()

    # 选择镜像复选框
    def check_image_checkbox(self):
        self.find_element(*ImageCenter.image_checkbox_loc).click()

    """
    以下为验证信息
    """
    # 登陆并进入镜像中心页面
    def login_into_ImageCenter(self):
        Login(self.driver).user_login()
        Page.open(self)
        # 此后为添加的验证，待续。。。
