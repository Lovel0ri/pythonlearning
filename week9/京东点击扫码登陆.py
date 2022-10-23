# @Time: 2022/10/23 12:20
# @Author: 李树斌
# @File : 京东点击扫码登陆.py
# @Software :PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.jd.com/')
    driver.find_element(By.LINK_TEXT, '你好，请登录').click()
    driver.find_element(By.LINK_TEXT, '账户登录').click()
    driver.find_element(By.LINK_TEXT, '扫码登录').click()
    driver.find_element(By.CSS_SELECTOR, '.qrcode-img > img').click()
    print('请在手机上扫码登录')
    input('登录成功后按回车键继续')
    #点击秒杀
    driver.find_element(By.LINK_TEXT, '秒杀').click()
    #点击秒杀商品
    driver.find_element(By.LINK_TEXT, '小米10至尊纪念版').click()

if __name__ == '__main__':
    main()