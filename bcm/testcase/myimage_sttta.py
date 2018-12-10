# -*- coding: utf-8 -*-
import unittest, random, sys
from bcm.testcase.models import function, publicunit, driver
from bcm.testcase.page_obj.MyImagePage import MyImage


class MyImageTst(publicunit.PublicTest):
    '''我的镜像界面测试'''

    # 部署镜像
    def test_1_deploy_image_test(self):
        '''我的镜像-部署镜像测试'''
        MyImage(self.driver).login_into_MyImage()
        MyImage(self.driver).deploy_image()
        po = MyImage(self.driver)
        self.assertEqual(po.deploy_image_success(), '创建服务')
        function.insert_img(self.driver, "MyImage_deploy_image.png")

    # 导出镜像
    def test_2_export_image_test(self):
        '''我的镜像-导出镜像测试'''
        MyImage(self.driver).login_into_MyImage()
        MyImage(self.driver).check_image_checkbox()
        MyImage(self.driver).export_image()
        function.insert_img(self.driver, "MyImage_export_image.png")

    # 收藏镜像
    def test_3_collect_image_test(self):
        '''我的镜像-收藏镜像测试'''
        MyImage(self.driver).login_into_MyImage()
        MyImage(self.driver).collect_image()
        function.insert_img(self.driver, "MyImage_collect_image.png")


"""    # 删除镜像
    def test_collect_image(self):
        MyImage(self.driver).login_into_Image()
        MyImage(self.driver).delete_image()
        # 此后为添加的验证，待续。。。
"""


if __name__ == "__main__":
    unittest.main()
