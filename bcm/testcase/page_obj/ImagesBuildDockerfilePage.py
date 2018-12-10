# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from bcm.testcase.page_obj.loginPage import Login
from time import sleep


class ImageBuildDockerfilePage(Page):
    '''
    dockerfile构建详情页
    '''
    url = '/ci/dockerfile'
    # define the fast images build item{

    image_name = (By.ID,"imgNameLast")                 # 镜像名称
    image_version = (By.ID,"imgNameVersion")          # 镜像版本
    public_properties = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[1]/div[2]/div/span/a[1]")      # 公有
    private_properties = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[1]/div[2]/div/span/a[2]")     # 私有
    image_type = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[2]/div/select")                         # 镜像种类下拉列表
    image_type_list = (By.XPATH, "/html/body/div[3]/article/div/div[2]/div/div/form/div[2]/div/select/option[1]")       # java
    abstract = (By.ID,"description")                     # 简介
    upload_button = (By.ID,"sourceCode")                 # 上传代码包
    import_mudule = (By.ID,"docImportBtn")               # 导入模板
    old_module = (By.XPATH,"/html/body/div[3]/article/div/div[3]/div[2]/div/table/tbody/tr[1]/td")   # 选择模板
    import_old_mudule_button = (By.XPATH,"/html/body/div[3]/article/div/div[3]/div[3]/a[1]")        # 导入
    cancel_import_button = (By.XPATH,"/html/body/div[3]/article/div/div[3]/div[3]/a[2]")            # 取消导入
    save_button = (By.ID,"docExportBtn")                   # 另存为模板
    new_module_name = (By.ID,"dockerFileTemplateName")    # 模板名
    save_new_mudule_button = (By.XPATH,"/html/body/div[3]/article/div/div[3]/div[3]/a[1]")        # 保存
    cancel_save_button = (By.XPATH,"/html/body/div[3]/article/div/div[3]/div[3]/a[2]")            # 取消保存
    dockerfile_content = (By.XPATH,"/html/body/div[3]/article/div/div[2]/div/div/form/div[6]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre") # 编写dockerfile
    project_name = (By.ID,"projectName")               # 项目名称
    create_button = (By.ID,"buildBtn")                  # 创建按钮


    # 填写镜像名称
    def write_image_name(self,imagename):
        self.find_element(*self.image_name).click()
        self.find_element(*self.image_name).send_keys(imagename)

    # 填写镜像版本
    def write_image_version(self,imageversion):
        self.find_element(*self.image_version).click()
        self.find_element(*self.image_version).send_keys(imageversion)

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
    def write_abstract(self,abstract):
        self.find_element(*self.abstract).click()
        self.find_element(*self.abstract).send_keys(abstract)

    # 上传代码
    def click_upload_button(self):
        self.find_element(*self.upload_button).click()

    # 导入旧的模板
    def click_import_module_button(self):
        self.find_element(*self.import_mudule).click()
        self.find_element(*self.old_module).click()
        self.find_element(*self.import_old_mudule_button).click()
        self.find_element(*self.cancel_import_button).click()

    # 另存为新的模板
    def click_save_button(self,newmodulename):
        self.find_element(*self.save_button).click()
        self.find_element(*self.new_module_name).click()
        self.find_element(*self.new_module_name).send_keys(newmodulename)
        self.find_element(*self.save_new_mudule_button).click()
        self.find_element(*self.cancel_save_button).click()

    # 输入项目项目名称
    def write_project_name(self):
        self.find_element(*self.project_name).click()

    # 编写dockerfile
    def write_dockerfile(self,dockerfile):
        self.find_element(*self.dockerfile_content).click()
        self.find_element(*self.dockerfile_content).send_keys(dockerfile)

    # 创建
    def click_create_button(self):
        self.find_element(*self.create_button).click()

# }define the Http item

# define the Http action{

# }define the Http action

