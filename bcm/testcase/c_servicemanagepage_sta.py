# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
# from models import publicunit, function
# from page_obj.loginPage import login
from bcm.testcase.models import function, publicunit
from bcm.testcase.page_obj.ServiceManagePage import ServiceMange
from bcm.testcase.page_obj.CreateServicePage import CreateService


class ServiceManageTest(publicunit.PublicTest):
    '''服务管理界面测试'''

    # 创建服务
    def test_0_create_service(self):
        '''创建服务测试'''
        ServiceMange(self.driver).login_into_service()
        ServiceMange(self.driver).create_service()
        CreateService(self.driver).find_image()
        CreateService(self.driver).input_service_name()
        CreateService(self.driver).input_chinese_name()
        CreateService(self.driver).input_person_name()
        CreateService(self.driver).input_telephone_number()
        CreateService(self.driver).input_person_email()
        CreateService(self.driver).input_web_path()
        CreateService(self.driver).import_template()
        CreateService(self.driver).finish_create_service()
        po = CreateService(self.driver)
        self.assertEqual(po.get_create_success_hit(), '服务管理')
        function.insert_img(self.driver, "create_service_success.png")


if __name__ == "__main__":
    unittest.main()
