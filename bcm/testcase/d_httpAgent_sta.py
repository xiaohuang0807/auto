# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
# from models import publicunit, function
# from page_obj.loginPage import login
from bcm.testcase.models import function, publicunit
from bcm.testcase.page_obj.loginPage import Login
from bcm.testcase.page_obj.HttpAgentPage import HttpAgentPage
from bcm.testcase.page_obj.HttpAgentStep1Page import HttpAgentStep1Page
from bcm.testcase.page_obj.HttpAgentStep2Page import HttpAgentStep2Page
from bcm.testcase.page_obj.HttpAgentUpdatePage import HttpAgentUpdatePage
from bcm.testcase.page_obj.ServiceManagePage import ServiceMange
from bcm.testcase.page_obj.HomePage import Navigation


class HttpAgent(publicunit.PublicTest):
    '''HTTP代理测试'''

    # 创建一个新的普通的http代理
    def test_create_http_agent(self):
        '''创建普通HTTP代理测试'''
        HttpAgentPage(self.driver).lonin_http_page()
        HttpAgentPage(self.driver).create_button()
        HttpAgentStep1Page(self.driver).write_service_name()
        HttpAgentStep1Page(self.driver).click_next_button()
        HttpAgentStep2Page(self.driver).write_domain_name()
        HttpAgentStep2Page(self.driver).write_visit_path()
        HttpAgentStep2Page(self.driver).write_service_port()
        HttpAgentStep2Page(self.driver).click_create_button()
        # Navigation(self.driver).click_service_integration()
        Navigation(self.driver).click_service_manage()
        po = ServiceMange(self.driver)
        self.assertEqual(po.get_http_link(), 'http://test.auto.bcm/versionone')
        function.insert_img(self.driver, "createHttpAgent.png")


if __name__ == "__main__":
    unittest.main()