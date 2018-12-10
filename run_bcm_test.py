from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

"""
#======================send email===============================================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", "utf-8")

    smtp = smtplib.SMTP
    smtp.connect("smtp.163.com")
    smtp.login("zheng_v@163.com", "123456")
    smtp.sendmail("gilbert_v@yeah.net", "testreport@163.com", msg.as_string())
    smtp.quit()
    print('email has benn sent out!')


#======= find the latest report by searching the report dir=====================
def new_report(testreport):
    lists = os.listdir(testreport)
    list.sort(key = lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_dir = './bcm/test_case'
    test_report = './bcm/report/'

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './bcm/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='bcm自动化测试报告', description='环境：win10 浏览器：Foxfire')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')

    runner.run(discover)
    fp.close()                                  # close the generated report
    file_path = new_report(test_report)         # search the report
    send_mail(file_path)                        # send the report email
"""


def send_mail(file_new):

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login('zheng_v@163.com', 'change2016..')
        smtp.sendmail("zheng_v@163.com", "gilbert_v@yeah.net", msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as err:
        print(err, "error: 邮箱发送失败！")
    # print("email send succeed !")


# ===================查找自动化测试报告，找到最新生成的测试报告文件===================
def new_report(testreport):

    lists = os.listdir(testreport)
    lists.sort(key = lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_dir = './bcm/testcase'
    test_report = './bcm/report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern = '*_sta.py')
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='bcm自动化测试报告', description='环境：win7 浏览器：Foxfire')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)



