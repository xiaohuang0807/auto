# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
# from models import publicunit, function
# from page_obj.loginPage import login
from bcm.testcase.models import function, publicunit
from bcm.testcase.page_obj.MyCollectionPage import MyCollection


class MyCollectionTst(publicunit.PublicTest):
    '''我的收藏界面测试'''

    # 部署镜像
    def test_1_deploy_image_my(self):
        '''我的收藏-部署服务测试'''
        MyCollection(self.driver).login_into_MyCollection()
        MyCollection(self.driver).deploy_image()
        po = MyCollection(self.driver)
        self.assertEqual(po.deploy_image_success(), '创建服务')
        function.insert_img(self.driver, "deploy_image.png")

    # 导出镜像
    def test_2_export_image_my(self):
        '''我的收藏-导出镜像测试'''
        MyCollection(self.driver).login_into_MyCollection()
        MyCollection(self.driver).check_image_checkbox()
        MyCollection(self.driver).export_image()

    # 收藏镜像
    def test_3_collect_image_my(self):
        '''我的收藏-收藏镜像测试'''
        MyCollection(self.driver).login_into_MyCollection()
        MyCollection(self.driver).collect_image()
        function.insert_img(self.driver, "collect_image_success.png")


if __name__ == "__main__":
    unittest.main()
