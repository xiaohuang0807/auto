# -*- coding: utf-8 -*-

from selenium import webdriver


def browser():
    driver = webdriver.Firefox()
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://bcm.bonc.pro")
    dr.quit()