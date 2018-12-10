# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login
from time import sleep


class ImageBuildFastPage(Page):
    '''
    快速构建详情页
    '''
    url = '/ci/addCodeSource'
    # define the fast images build item{

    base_image= (By.ID,"baseImageName")               # 基础镜像
    base_image_list = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[1]/div[1]/div/select[1]/option[2]")
    base_image_version = (By.ID,"baseImageId")        # 基础镜像版本
    base_image_version_list = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[1]/div[1]/div/select[2]/option[1]")
    image_name = (By.ID,"imgNameLast")                 # 镜像名称
    image_version = (By.ID,"imgNameVersion")          # 镜像版本
    public_properties = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[1]/div[3]/div/span/a[1]")      # 公有
    private_properties = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[1]/div[3]/div/span/a[2]")     # 私有
    image_type = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[2]/div/select")                         # 镜像种类下拉列表
    image_type_list = (By.XPATH, "/html/body/div[3]/article/div/div[2]/div/div/form/div[2]/div/select/option[1]")
    abstract = (By.ID,"description")                   # 简介
    upload_button = (By.ID,"sourceCode")               # 上传代码包
    project_name = (By.ID,"projectName")               # 项目名称
    create_button = (By.ID,"buildBtn")                  # 创建按钮

    # 选择基础镜像
    def click_base_image(self):
        self.find_element(*self.base_image).click()
        self.find_element(*self.base_image_list).click()

    # 选择基础镜像版本
    def click_base_image_version(self):
        self.find_element(*self.base_image_version).click()
        self.find_element(*self.base_image_version_list).click()

    # 填写镜像名称
    def write_image_name(self):
        self.find_element(*self.image_name).click()
        self.find_element(*self.image_name).send_keys("autotest")

    # 填写镜像版本
    def write_image_version(self):
        self.find_element(*self.image_version).click()
        self.find_element(*self.image_version).clear()
        self.find_element(*self.image_version).send_keys("20181122")

    # 公有
    def click_public_properties(self):
        self.find_element(*self.public_properties).click()

    # 私有
    def click_private_properties(self):
        self.find_element(*self.private_properties).click()

    # 选择镜像种类
    def click_image_type(self):
        self.find_element(*self.image_type).click()
        self.find_element(*self.image_type_list).click()

    # 输入简介
    def write_abstract(self):
        self.find_element(*self.abstract).click()
        self.find_element(*self.abstract).send_keys("测试自动化脚本")

    # 上传代码
    def click_upload_button(self):
        # self.find_element(*self.upload_button).click()
        self.find_element(*self.upload_button).send_keys("D:\\versionone.war")

    # 输入项目项目名称
    def write_project_name(self):
        self.find_element(*self.project_name).click()
        self.find_element(*self.project_name).send_keys("autotest")

    # 创建
    def click_create_button(self):
        self.find_element(*self.create_button).click()

# }define the Http item

# define the Http action{

# }define the Http action

