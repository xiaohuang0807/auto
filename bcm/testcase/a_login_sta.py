# -*- coding: utf-8 -*-

from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
# from models import publicunit, function
# from page_obj.loginPage import login
from bcm.testcase.models import function, publicunit
from bcm.testcase.page_obj.loginPage import Login


class loginTest(publicunit.PublicTest):
    '''登录测试'''

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_login5(self):
        '''用户名和密码正确'''
        self.user_login_verify(username="zhengyin", password="zhengyin1234")
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), 'zhengyin')
        function.insert_img(self.driver, "user_password_true.png")
        sleep(5)


if __name__ == '__main__':
    unittest.main()
