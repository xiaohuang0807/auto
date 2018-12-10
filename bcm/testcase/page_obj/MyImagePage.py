# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login


class MyImage(Page):
    '''
    我的镜像界面
    '''
    url = '/registry/1'

    deploy_image_loc = (By.XPATH, '//*[@id="imageList"]/tr/td[9]/a[1]/i')    # 获取部署镜像按钮
    export_image_loc = (By.XPATH, '//*[@id="imageList"]/tr/td[9]/a[2]/i')    # 获取导出镜像按钮
    collect_image_loc = (By.XPATH, '//*[@id="imageList"]/tr/td[9]/a[3]/i')   # 获取收藏镜像按钮
    delete_image_loc = (By.XPATH, '//*[@id="imageList"]/tr/td[9]/a[4]/i')    # 获取删除镜像按钮
    find_input_loc = (By.XPATH, '//*[@id="DataTables_Table_0_filter"]/label/input')  # 获取查找输入框
    all_checkbox_loc = (By.ID, "checkallbox")         # 获取所有复选框按钮
    image_checkbox_loc = (By.NAME, "ids")             # 获取镜像复选框按钮
    refresh_ImagePage_loc = (By.XPATH, '//a[@id="volReloadBtn"]/i')  # 获取刷新页面按钮
    BatchDelete_image_loc = (By.XPATH, '//*[@id="deleteButton"]/i')  # 获取批量删除镜像按钮
    name_checkbox_loc = (By.XPATH, '//*[@id="accordion2"]/div/div[1]/h4/input')         # 获取按名称所有复选框按钮
    time_checkbox_loc = (By.XPATH, '//*[@id="accordion3"]/div/div[1]/h4/input')         # 获取按时间所有复选框按钮
    ConfirmDelete_btn_loc = (By.LINK_TEXT, "确定删除")
    confirm_btn_loc = (By.LINK_TEXT, "确定")
    deploy_image_success_loc = (By.XPATH, "/html/body/div[3]/article/div/div[1]/ol/li[5]")


    # 部署镜像
    def deploy_image(self):
        self.find_element(*MyImage.deploy_image_loc).click()

    # 导出镜像
    def export_image(self):
        self.find_element(*MyImage.export_image_loc).click()

    # 收藏镜像
    def collect_image(self):
        self.find_element(*MyImage.collect_image_loc).click()

    # 删除镜像
    def delete_image(self):
        self.find_element(*MyImage.delete_image_loc).click()
        self.find_element(*MyImage.confirm_btn_loc).click()

    # 按名称批量删除镜像
    def name_batch_delete_image(self):
        self.find_element(*MyImage.BatchDelete_image_loc).click()
        self.find_element(*MyImage.name_checkbox_loc).click()
        self.find_element(*MyImage.ConfirmDelete_btn_loc).click()

    # 按时间批量删除镜像
    def time_batch_delete_image(self):
        self.find_element(*MyImage.BatchDelete_image_loc).click()
        self.find_element(*MyImage.time_checkbox_loc).click()
        self.find_element(*MyImage.ConfirmDelete_btn_loc).click()

    # 刷新页面
    def refresh_image_page(self):
        self.find_element(*MyImage.refresh_ImagePage_loc).click()

    # 查找输入框
    def find_input(self):
        self.find_element(*MyImage.find_input_loc).click()

    # 选择所有复选框
    def check_all_checkbox(self):
        self.find_element(*MyImage.all_checkbox_loc).click()

    # 选择镜像复选框
    def check_image_checkbox(self):
        self.find_element(*MyImage.image_checkbox_loc).click()

    # 选择按名称所有复选框
    def name_checkbox(self):
        self.find_element(*MyImage.name_checkbox_loc).click()

    # 选择按时间所有复选框
    def time_checkbox(self):
        self.find_element(*MyImage.time_checkbox_loc).click()

    """
    以下为验证信息
    """
    # 进入镜像中心页面
    def login_into_MyImage(self):
        Login(self.driver).user_login()
        Page.open(self)
        # 此后为添加的验证，待续。。。

    # 获取部署镜像，验证成功
    def deploy_image_success(self):
        return self.find_element(*self.deploy_image_success_loc).text




    
