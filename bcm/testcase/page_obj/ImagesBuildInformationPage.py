# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login
from time import sleep


class ImagesBuildInformationPage(Page):
    '''
    构建信息
    '''
    url = '/ci/detail/1941'   # 地址会变
    # define the fast images build item{

    fast_deploy= (By.ID,"deploy")       # 快速部署
    rebuild = (By.ID,"replayci")        # 重新构建
    build_log = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[1]")         # 构建日志

    base_setting = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[2]")      # 基本设置
    project_name = (By.ID, "projectName")  # 项目名称
    abstract = (By.ID, "description")      # 简介
    image_type = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[4]/div[2]/form/div[3]/div/select")     # 镜像种类下拉列表
    image_type_list = (By.XPATH, "/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[4]/div[2]/form/div[3]/div/select/option[1]")
    upload_button = (By.ID,"sourceCode")              # 重新上传代码文件
    base_image= (By.ID,"baseImageName")               # 基础镜像
    base_image_list = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[4]/div[2]/form/div[6]/div/select[1]/option[1]")
    base_image_version = (By.ID, "baseImageId")       # 基础镜像版本
    base_image_version_list = (By.XPATH, "/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[4]/div[2]/form/div[6]/div/select[2]/option[1]")
    confirm_modify_button = (By.ID, "editCiUploadCodeBtn")     # 确认修改按钮

    operate = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div[1]/div[2]/div[3]")     # 操作
    delete_project = (By.ID,"delCiBtn")     # 删除项目


    # 快速部署
    def click_fast_deploy(self):
        self.find_element(*self.fast_deploy).click()

    # 重新构建
    def click_rebuild(self):
        self.find_element(*self.rebuild).click()

    # 构建日志
    def click_build_log(self):
        self.find_element(*self.build_log).click()

    # 基本设置
    def click_base_setting(self):
        self.find_element(*self.base_setting).click()

    def modify_project_name(self):
        self.find_element(*self.project_name).click()
        self.find_element(*self.project_name).send_keys(self.projectname)

    def modify_abstract(self):
        self.find_element(*self.abstract).click()
        self.find_element(*self.abstract).send_keys(self.abstract)

    def modify_image_type(self):
        self.find_element(*self.image_type).click()
        self.find_element(*self.image_type_list).click()

    def modify_code_package(self):
        self.find_element(*self.upload_button).click()

    def modify_base_image(self):
        self.find_element(*self.base_image).click()
        self.find_element(*self.base_image_list).click()

    def modify_base_image_version(self):
        self.find_element(*self.base_image_version).click()
        self.find_element(*self.base_image_version_list).click()

    def modify_confirm_button(self):
        self.find_element(*self.confirm_modify_button).click()

    def click_operate(self):
        self.find_element(*self.operate).click()

    def click_operate_delete_project(self):
        self.find_element(*self.delete_project).click()



# }define the Http item

# define the Http action{

# }define the Http action

