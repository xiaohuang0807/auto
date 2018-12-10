# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login
from time import sleep


class ImageBuildListPage(Page):
    '''
    镜像构建列表页
    '''
    url = '/ci'
    # define the images build item{

    fast_build_button = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a[1]/i")           # 快速构建
    upload_image_build_button = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a[2]/i")   # 上传镜像
    dockerfile_build_button = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a[3]/i")     # dockerfile构建
    add_button = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a[4]/i")                  # 添加
    reload_button = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a[5]/i")               # 刷新按钮
    search_input = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/label/input")      # 查找框
    project_name = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/a")           # 项目名称   变化
    image = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]/td[6]")                    # 镜像    变化
    build_button = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]/td[7]/span/i")     # 构建按钮

    # 验证
    status = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]")

    # 快速构建按钮
    def click_fast_build_button(self):
        self.find_element(*self.fast_build_button).click()

    # 上传镜像按钮
    def click_upload_image_build_button(self):
        self.find_element(*self.upload_image_build_button).click()

    # dockerfile构建按钮
    def click_dockerfile_build_button(self):
        self.find_element(*self.dockerfile_build_button).click()

    # 添加按钮
    def click_add_button(self):
        self.find_element(*self.add_button).click()

    # 刷新按钮
    def click_reload_button(self):
        self.find_element(*self.reload_button).click()

    # 查找按钮
    def input_search(self, project_name):
        self.find_element(*self.search_input).click()
        self.find_element(*self.search_input).send_keys(project_name)

    # 项目名称
    def click_project_name(self):
        self.find_element(*self.project_name).click()

    # 镜像
    def click_image(self):
        self.find_element(*self.image).click()

    # 构建按钮
    def click_build_button(self):
        self.find_element(*self.build_button).click()

    # 验证是否有新创建的镜像
    def get_error_hint(self):
        return self.find_element(*self.status).text

    # 登录到镜像构建
    def lonin_images_build_page(self):
        Login(self.driver).user_login()
        Page.open(self)

# }define the Http item

# define the Http action{

# }define the Http action

