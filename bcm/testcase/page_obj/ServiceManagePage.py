# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from bcm.testcase.page_obj.loginPage import Login
from selenium.webdriver.common.by import By
from bcm.testcase.page_obj.base import Page
from time import sleep


class ServiceMange(Page):
    '''
    服务管理界面
    '''
    url = '/service'

    create_service_btn_loc = (By.XPATH, '//*[@id="serviceCreateBtn"]/i')    # 获取创建服务按钮
    start_service_loc = (By.ID, "startContainerFa")                         # 获取启动服务按钮
    stop_service_loc = (By.ID, "stopContainerFa")                           # 获取停止服务按钮
    delete_service_loc = (By.ID, "deleteButtonFa")                          # 获取删除服务按钮
    export_service_loc = (By.ID, "ExportButtonFa")                          # 获取导出服务按钮
    refresh_servicepage_loc = (By.XPATH, '//*[@id="serviceReloadBtn"]/i')   # 获取刷新页面按钮
    find_input_loc = (By.XPATH, '//*[@id="DataTables_Table_0_filter"]/label/input') # 获取查找输入框
    all_checkbox_loc = (By.ID, "checkallbox")                               # 获取所有复选框按钮
    confirm_btn_loc = (By.LINK_TEXT, "确定")                                # 获取停止操作弹框确定按钮
    # 弹性伸缩元素
    more_configuration_loc = (By.XPATH, '//*[@id="2081_moreFun"]/i')        # 获取更能多配置按钮
    rubber_sheeting_loc = (By.ID, "2081_scaleCluster")                      # 获取弹性伸缩按钮
    number_instances_loc = (By.ID, "numberChange")                          # 获取实例数量文本框
    btn_to_loc = (By.LINK_TEXT, "确定")                                     # 获取弹性伸缩确定按钮
    # 更改配置元素
    more_configuration4_loc = (By.XPATH, '//*[@id="2119_moreFun"]/i')       # 获取ID为2119的更多配置按钮
    stop_this_service_loc = (By.XPATH, '//*[@id="2119_stop"]/i')            # 获取ID为2082的停止按钮
    btn_of_stop_service_loc = (By.LINK_TEXT, "确定")                        # 获取停止当前服务的确定按钮
    change_configuration_loc = (By.ID, "2119_changeConfiguration")       # 获取更改配置按钮
    checkbox_of_cpu_loc = (By.XPATH, '//*[@id="changeConf"]/ul/li[2]/div[1]/label[1]/input')  # 获取CPU选择框
    checkbox_of_memory_loc = (By.XPATH, '//*[@id="changeConf"]/ul/li[3]/div[1]/label[1]/input') # 获取内存选择框
    btn_of_configuration_loc = (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]') # 获取确定按钮
    start_this_service_loc = (By.XPATH, '//*[@id="2119_start"]/i')          # 获取ID为2119的启动按钮
    # 自动伸缩元素
    more_configuration2_loc = (By.XPATH, '//*[@id="2082_moreFun"]/i')       # 获取ID为2082的更多配置按钮
    auto_flexing_btn_loc = (By.ID, "2082_autoFlex")                         # 获取自动伸缩按钮
    usage_rate_btn_loc = (By.ID, "targetCPUUtilizationPercentage")          # 获取CPU使用率文本框
    min_replicas_loc = (By.ID, "minReplicas")                               # 获取最小实例数文本框
    max_replicas_loc = (By.ID, "maxReplicas")                               # 获取最大实例数文本框
    btn_of_create_loc = (By.LINK_TEXT, "创建")                              # 获取创建自动伸缩按钮
    btn_of_delete_loc = (By.LINK_TEXT, "删除")                              # 获取删除自动伸缩按钮
    # 定时伸缩元素
    more_configuration3_loc = (By.XPATH, '//*[@id="2083_moreFun"]/i')       # 获取ID为2083的更多配置按钮
    time_scale_loc = (By.XPATH, '//ul[@id="2083_dropdown"]/li[3]/a[3]')     # 获取定时伸缩按钮
    add_strategy_list_loc = (By.ID, "strategyRelate_add_strategyList")      # 获取新增策略按钮
    checkbox_name_loc = (By.NAME, "strategyCheck")                          # 获取策略名
    select_service_checkbox_loc = (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]') # 选择服务策略
    btn_create_of_loc = (By.LINK_TEXT, "确定")                              # 确定选择
    # 验证信息元素
    get_service_status_loc = (By.XPATH, '//*[@id="serviceList"]/tr/td[4]/a')  # 获取服务运行状态
    service_status_loc = (By.XPATH, '//*[@id="serviceList"]/tr[2]/td[4]/a')  # 获取服务运行状态

    # 验证
    service_addr = (By.XPATH, '//*[@id="serviceList"]/tr[6]/td[6]/a')

    # 创建服务
    def create_service(self):
        self.find_element(*ServiceMange.create_service_btn_loc).click()

    # 停止服务
    def stop_service(self):
        self.find_element(*ServiceMange.all_checkbox_loc).click()
        self.find_element(*ServiceMange.stop_service_loc).click()
        self.find_element(*ServiceMange.confirm_btn_loc).click()

    # 启动服务
    def start_service(self):
        self.find_element(*ServiceMange.all_checkbox_loc).click()
        self.find_element(*ServiceMange.start_service_loc).click()
        self.find_element(*ServiceMange.confirm_btn_loc).click()

    # 删除服务
    def delete_service(self):
        self.find_element(*ServiceMange.delete_service_loc).click()
        self.find_element(*ServiceMange.confirm_btn_loc).click()

    # 导出服务
    def export_service(self):
        self.find_element(*ServiceMange.export_service_loc).click()

    # 刷新页面
    def refresh_service_page(self):
        self.find_element(*ServiceMange.refresh_servicepage_loc).click()

    # 弹性伸缩操作
    def rubber_sheeting(self):
        self.find_element(*ServiceMange.more_configuration_loc).click()
        self.find_element(*ServiceMange.rubber_sheeting_loc).click()
        self.find_element(*ServiceMange.number_instances_loc).clear()
        self.find_element(*ServiceMange.number_instances_loc).send_keys(2)
        self.find_element(*ServiceMange.number_instances_loc).click()
        self.find_element(*ServiceMange.btn_to_loc).click()

    # 版本升级
    def version_upgrade(self):
        ...

    # 更改配置
    def change_configuration(self):
        self.find_element(*ServiceMange.stop_this_service_loc).click()
        self.find_element(*ServiceMange.btn_of_stop_service_loc).click()
        sleep(5)
        self.find_element(*ServiceMange.more_configuration4_loc).click()
        sleep(2)
        self.find_element(*ServiceMange.change_configuration_loc).click()
        sleep(2)
        self.find_element(*ServiceMange.checkbox_of_cpu_loc).click()
        sleep(2)
        self.find_element(*ServiceMange.checkbox_of_memory_loc).click()
        sleep(2)
        self.find_element(*ServiceMange.btn_of_configuration_loc).click()
        sleep(2)
        self.find_element(*ServiceMange.start_this_service_loc).click()
        sleep(5)

    # 创建自动伸缩策略
    def service_auto_scaling(self):
        self.find_element(*ServiceMange.more_configuration2_loc).click()
        self.find_element(*ServiceMange.auto_flexing_btn_loc).click()
        self.find_element(*ServiceMange.usage_rate_btn_loc).click()
        self.find_element(*ServiceMange.usage_rate_btn_loc).clear()
        self.find_element(*ServiceMange.usage_rate_btn_loc).send_keys(80)
        self.find_element(*ServiceMange.min_replicas_loc).click()
        self.find_element(*ServiceMange.min_replicas_loc).clear()
        self.find_element(*ServiceMange.min_replicas_loc).send_keys(1)
        self.find_element(*ServiceMange.max_replicas_loc).click()
        self.find_element(*ServiceMange.max_replicas_loc).clear()
        self.find_element(*ServiceMange.max_replicas_loc).send_keys(2)
        self.find_element(*ServiceMange.btn_of_create_loc).click()

    # 删除自动伸缩策略
    def service_auto_scaling_delete(self):
        self.find_element(*ServiceMange.more_configuration2_loc).click()
        self.find_element(*ServiceMange.auto_flexing_btn_loc).click()
        self.find_element(*ServiceMange.btn_of_delete_loc).click()

    # 创建定时伸缩策略
    def service_timed_task(self):
        self.find_element(*ServiceMange.more_configuration3_loc).click()
        self.find_element(*ServiceMange.time_scale_loc).click()
        self.find_element(*ServiceMange.add_strategy_list_loc).click()
        self.find_element(*ServiceMange.checkbox_name_loc).click()
        self.find_element(*ServiceMange.select_service_checkbox_loc).click()
        self.find_element(*ServiceMange.btn_create_of_loc).click()

    #
    """
    以下为验证信息
    """
    # 登陆并进入服务管理页面
    def login_into_service(self):
        Login(self.driver).user_login()
        Page.open(self)

    # 验证是否有访问地址
    def get_http_link(self):
        return self.find_element(*self.service_addr).text

'''
    # 验证集群运行状态
    def get_service_status(self):
        return self.find_element(*ServiceMange.get_service_status_loc).text
'''


