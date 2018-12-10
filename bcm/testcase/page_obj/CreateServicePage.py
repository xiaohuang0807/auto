# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from bcm.testcase.page_obj.ServiceManagePage import ServiceMange
from bcm.testcase.page_obj.loginPage import Login
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep


class CreateService(Page):
    '''
    镜像选择界面
    '''
    url = '/service/add'

    # /service/add镜像来源页面
    select_image_loc = (By.XPATH, '//*[@id="imageList"]/li[115]/span[4]/div/span[2]')
    select_input_image_loc = (By.XPATH, '//*[@id="imageName"]')
    select_btn_loc = (By.XPATH, '//*[@id="searchimage"]')
    select_click_image_loc = (By.XPATH, '//*[@id="imageList"]/li[6]/span[3]/div/span[2]')
    # /service/add容器配置页面
    service_name_loc = (By.ID, "serviceName")  # 获取服务名称input控件
    service_chinese_name_loc = (By.XPATH, '//*[@id="serviceChName"]')  # 获取服务中文名称input控件
    person_in_charge_loc = (By.ID, "responsiblePerson")  # 获取责任人input控件
    telephone_number_loc = (By.ID, "responsiblePersonTelephone")  # 获取责任人电话input控件
    person_mail_loc = (By.ID, "responsiblePersonEmail")  # 获取责任人邮箱input控件
    service_access_path_loc = (By.ID, "webPath")  # 获取服务访问路径input控件
    conversation_loc = (By.ID, "sessionAffinity")  # 获取会话黏连方式控件
    import_template_loc = (By.ID, "importBtn")  # 获取导入模板按钮控件
    select_environment_variable_loc = (By.XPATH, '//*[@id="Path-env"]/tr/td')  # 获取模板控件
    import_btn_loc = (By.LINK_TEXT, "导入")  # 获取导入按钮控件
    create_btn_loc = (By.ID, "createButton")  # 获取创建按钮控件
    create_error_hint_loc = (By.XPATH, '/html/body/div[7]/div[2]')
    create_success_loc = (By.XPATH, '/html/body/div[3]/article/div/div[1]/ol/li[3]')

    # 选择镜像进行部署服务
    def click_image_btn(self):
        self.find_element(*CreateService.select_image_loc).click()

    # 通过镜像名称搜索镜像
    def find_image(self):
        self.find_element(*CreateService.select_input_image_loc).click()
        self.find_element(*CreateService.select_input_image_loc).clear()
        self.find_element(*CreateService.select_input_image_loc).send_keys("demo")
        self.find_element(*CreateService.select_btn_loc).click()
        self.find_element(*CreateService.select_click_image_loc).click()

    # 输入服务名称
    def input_service_name(self):
        self.find_element(*CreateService.service_name_loc).click()
        self.find_element(*CreateService.service_name_loc).clear()
        self.find_element(*CreateService.service_name_loc).send_keys("demosix")

    # 输入服务中文名称
    def input_chinese_name(self):
        self.find_element(*CreateService.service_chinese_name_loc).click()
        self.find_element(*CreateService.service_chinese_name_loc).clear()
        self.find_element(*CreateService.service_chinese_name_loc).send_keys("镜像")

    # 输入责任人信息
    def input_person_name(self):
        self.find_element(*CreateService.person_in_charge_loc).click()
        self.find_element(*CreateService.person_in_charge_loc).clear()
        self.find_element(*CreateService.person_in_charge_loc).send_keys("zhengyin")

    # 输入责任人电话
    def input_telephone_number(self):
        self.find_element(*CreateService.telephone_number_loc).click()
        self.find_element(*CreateService.telephone_number_loc).clear()
        self.find_element(*CreateService.telephone_number_loc).send_keys("12345678900")

    # 输入责任人邮箱
    def input_person_email(self):
        self.find_element(*CreateService.person_mail_loc).click()
        self.find_element(*CreateService.person_mail_loc).clear()
        self.find_element(*CreateService.person_mail_loc).send_keys("qwer@qq.com")

    # 输入服务访问路径
    def input_web_path(self):
        self.find_element(*CreateService.service_access_path_loc).click()
        self.find_element(*CreateService.service_access_path_loc).clear()
        self.find_element(*CreateService.service_access_path_loc).send_keys("demosix")

    # 添加环境变量
    def import_template(self):
        ActionChains(self.driver).move_by_offset(10, 100).perform()
        sleep(5)
        self.find_element(*CreateService.import_template_loc).click()
        self.find_element(*CreateService.select_environment_variable_loc).click()
        self.find_element(*CreateService.import_btn_loc).click()

    # 完成创建操作
    def finish_create_service(self):
        self.find_element(*CreateService.create_btn_loc).click()

    # 登录到镜像选择界面
    def into_select_image(self):
        Login(self.driver).user_login()
        Page.open(self)

    # 获取失败验证信息
    def get_create_error_hint(self):
        return self.find_element(*self.create_error_hint_loc).text

    # 获取创建成功的信息
    def get_create_success_hit(self):
        return self.find_element(*self.create_success_loc).text

