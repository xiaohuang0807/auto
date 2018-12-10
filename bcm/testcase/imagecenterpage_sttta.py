# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
# from models import publicunit, function
# from page_obj.loginPage import login
from bcm.testcase.models import function, publicunit
from bcm.testcase.page_obj.ImageCenterPage import ImageCenter


class ImageCenterTst(publicunit.PublicTest):
    '''镜像中心界面测试'''

    # 部署镜像
    def test_1_deploy_image(self):
        '''镜像中心-部署镜像测试'''
        ImageCenter(self.driver).login_into_ImageCenter()
        ImageCenter(self.driver).deploy_image()
        function.insert_img(self.driver, "deploy_image_success.png")

    # 导出镜像
    def test_2_export_image(self):
        '''镜像中心-导出镜像测试'''
        ImageCenter(self.driver).login_into_ImageCenter()
        ImageCenter(self.driver).check_image_checkbox()
        ImageCenter(self.driver).export_image()
        function.insert_img(self.driver, "export_image_success.png")

    # 收藏镜像
    def test_3_collect_image(self):
        '''镜像中心-收藏镜像测试'''
        ImageCenter(self.driver).login_into_ImageCenter()
        ImageCenter(self.driver).collect_image()
        function.insert_img(self.driver, "collect_image_success.png")


if __name__ == "__main__":
    unittest.main()
