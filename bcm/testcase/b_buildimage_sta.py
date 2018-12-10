# -*- coding: utf-8 -*-
from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
# from models import publicunit, function
# from page_obj.loginPage import login
from bcm.testcase.models import function, publicunit
from bcm.testcase.page_obj.loginPage import Login
from bcm.testcase.page_obj.ImagesBuildListPage import ImageBuildListPage
from bcm.testcase.page_obj.ImagesBuildFastPage import ImageBuildFastPage


class BuildImage(publicunit.PublicTest):
    '''构建镜像测试'''
    # 创建一个镜像
    def test_create_image(self):
        '''构建镜像测试'''
        ImageBuildListPage(self.driver).lonin_images_build_page()
        ImageBuildListPage(self.driver).click_fast_build_button()
        ImageBuildFastPage(self.driver).click_base_image()
        ImageBuildFastPage(self.driver).click_base_image_version()
        ImageBuildFastPage(self.driver).write_image_name()
        ImageBuildFastPage(self.driver).write_image_version()
        ImageBuildFastPage(self.driver).click_private_properties()
        ImageBuildFastPage(self.driver).click_image_type()
        ImageBuildFastPage(self.driver).write_abstract()
        ImageBuildFastPage(self.driver).click_upload_button()
        ImageBuildFastPage(self.driver).write_project_name()
        ImageBuildFastPage(self.driver).click_create_button()
        self.driver.implicitly_wait(30)
        ImageBuildListPage(self.driver).click_build_button()
        self.driver.implicitly_wait(20)
        # ImageBuildListPage(self.driver).lonin_images_build_page()
        po = ImageBuildListPage(self.driver)
        self.assertEqual(po.get_error_hint(), '构建中')
        function.insert_img(self.driver, "imagebuild.png")


if __name__ == "__main__":
    unittest.main()