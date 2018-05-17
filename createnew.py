# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        #driver.get("http://172.16.3.117:8001/manager/tenant/")
        driver.get("http://172.16.3.117:8001/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Changeme")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//ul[@id='toolbarfirst']/li[4]/a/span/i").click()
        driver.find_element_by_xpath("//ul[@id='toolbarfirst']/li[4]/ul/li[2]/a/span").click()
        driver.find_element_by_id("page-content").click()
        driver.find_element_by_link_text(u"新建").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"测试组")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"北京")
        driver.find_element_by_name("contacts").click()
        driver.find_element_by_name("contacts").clear()
        driver.find_element_by_name("contacts").send_keys("yangzhidong")
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("1111111111111111111111111111")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("yangzhidong@bonc.com.cn")
        driver.find_element_by_name("tenantAdmin").click()
        driver.find_element_by_name("tenantAdmin").click()
        driver.find_element_by_name("tenantAdmin").clear()
        driver.find_element_by_name("tenantAdmin").send_keys("adminyang")
        driver.find_element_by_id("available7").click()        
        
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try: self.assertEqual(u"测试组", driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+"\n:test_001")
        try: self.assertEqual(u"北京", driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("yangzhidong", driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("1111111111111111111111111211", driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+"\n:test_002")
        try: self.assertEqual("yangzhidong@bonc.com.cn", driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td[5]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("adminyang", driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td[6]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//table[@id='org_table']/tbody/tr[3]/td[7]").click()
		
		
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
