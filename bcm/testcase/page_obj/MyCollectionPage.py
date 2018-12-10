# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login


class MyCollection(Page):
    '''
    我的收藏界面
    '''
    url = '/registry/2'

    deploy_image_loc = (By.XPATH, '//*[@id="imageList"]/tr[1]/td[9]/a[1]')     # 获取部署镜像按钮
    export_image_loc = (By.XPATH, '//*[@id="imageList"]/tr[1]/td[9]/a[2]')     # 获取导出镜像按钮
    collect_image_loc = (By.XPATH, '//*[@id="imageList"]/tr[1]/td[9]/a[3]')    # 获取收藏镜像按钮
    refresh_imagepage_loc = (By.XPATH, '//*[@id="volReloadBtn"]/i')              # 获取刷新页面按钮
    find_input_loc = (By.XPATH, '//*[@id="DataTables_Table_0_filter"]/label/input')  # 获取查找输入框
    delete_image_loc = (By.ID, '//*[@id="imageList"]/tr[3]/td[9]/a[4]/i')        # 获取删除镜像按钮
    all_checkbox_loc = (By.ID, "checkallbox")         # 获取所有复选框按钮
    image_checkbox_loc = (By.NAME, "ids")             # 获取镜像复选框按钮
    confirm_btn_loc = (By.LINK_TEXT, "确定")
    deploy_image_success_loc = (By.XPATH, "/html/body/div[3]/article/div/div[1]/ol/li[5]")

    # 部署镜像
    def deploy_image(self):
        self.find_element(*MyCollection.deploy_image_loc).click()

    # 导出镜像
    def export_image(self):
        self.find_element(*MyCollection.export_image_loc).click()

    # 收藏镜像
    def collect_image(self):
        self.find_element(*MyCollection.collect_image_loc).click()

    # 刷新页面
    def refresh_image_page(self):
        self.find_element(*MyCollection.refresh_imagepage_loc).click()

    # 查找输入框
    def find_input(self):
        self.find_element(*MyCollection.find_input_loc).click()

    # 选择所有复选框
    def check_all_checkbox(self):
        self.find_element(*MyCollection.all_checkbox_loc).click()

    # 选择镜像复选框
    def check_image_checkbox(self):
        self.find_element(*MyCollection.image_checkbox_loc).click()

    # 删除镜像
    def delete_service(self):
        self.find_element(*MyCollection.delete_service_loc).click()
        self.find_element(*MyCollection.confirm_btn_loc).click()

    """
    以下为验证信息
    """
    # 登陆并进入我的收藏页面
    def login_into_MyCollection(self):
        Login(self.driver).user_login()
        Page.open(self)
        # 此后为添加的验证，待续。。。

    # 获取部署镜像，验证成功
    def deploy_image_success(self):
        return self.find_element(*self.deploy_image_success_loc).text

