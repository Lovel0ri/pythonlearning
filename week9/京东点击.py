# @Time: 2022/10/23 11:05
# @Author: 李树斌
# @File : 京东点击.py
# @Software :PyCharm
import time
from requests import request
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import cv2_tools
import numpy as np

from datetime import datetime
jd_id = '17727134766'
jd_pwd = 'aA2697601945'

driver = webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.find_element(By.LINK_TEXT, "你好，请登录").click()
driver.find_element(By.LINK_TEXT, "账户登录").click()
driver.find_element(By.ID, "loginname").send_keys(jd_id)
driver.find_element(By.ID, "nloginpwd").send_keys(jd_pwd)
driver.find_element(By.ID, "loginsubmit").click()

#计算滑动距离
distance = driver.find_element(By.CLASS_NAME, "JDJRV-bigimg").size['width'] - driver.find_element(By.CLASS_NAME, "JDJRV-smallimg").size['width']
time.sleep(3)
#滑动滑块
webdriver.ActionChains(driver).click_and_hold(driver.find_element(By.CLASS_NAME, "JDJRV-slide-btn")).perform()

# 获取验证码中的图片
def get_image(driver):
    # 获取验证码中的img标签中的src

    image_url = driver.find_element(By.CLASS_NAME, "JDJRV-bigimg").get_attribute('src')
    print(image_url)
    #获取移动块url
    block_url = driver.find_element(By.CLASS_NAME, "JDJRV-smallimg").get_attribute('src')
    req = request.Request(image_url)
    bg = open('bg.png', 'wb')
    bg.write(request.urlopen(req).read())
    bg.close()
    req = request.Request(block_url)
    fullbg = open('fullbg.png', 'wb')
    fullbg.write(request.urlopen(req).read())
    fullbg.close()
    return 'bg.png', 'fullbg.png'

bkg, blk= get_image(driver)

# 计算缺口的位置，由于缺口位置查找偶尔会出现找不准的现象，这里进行判断，如果查找的缺口位置x坐标小于100，
# 我们进行刷新验证码操作，重新计算缺口位置，知道满足条件位置。
def get_distance(bkg, blk):
        # 读取灰度图
        block = cv2_tools.imread(blk, 0)
        tp = cv2_tools.imread(bkg, 0)
        # 保存图像
        cv2_tools.imwrite('bg.png', tp)
        cv2_tools.imwrite('fullbg.png', block)

        block = cv2_tools.imread('fullbg.png')
        block = cv2_tools.cvtColor(block, cv2_tools.COLOR_BGR2GRAY)
        block = abs(255 - block)
        cv2_tools.imwrite('fullbg.png', block)
        block = cv2_tools.imread('fullbg.png')
        tp = cv2_tools.imread('bg.png')
        ''' 
        模板匹配函数 cv2.matchTemplate(image, temp, method, result=None, mask=None)
        image：待搜索图像;temp：模板图像;result：匹配结果;method：计算匹配程度的方法
        '''
        result = cv2_tools.matchTemplate(block, 'bg.png', cv2_tools.TM_CCOEFF_NORMED)
        mn_val, max_val, min_loc, max_loc = cv2_tools.minMaxLoc(result)
        # x, y = np.unravel_index(result.argmax(), result.shape)
        # x, y, w, h = cv2.boundingRect(GrayImage)
        print(min_loc, max_loc)
        # min_loc = (164, 58) # (y, x)
        # max_loc = (170, 103) # (y, x)
        # x取最小值(如果x<10，取最大值），y取最大值（如果y>200 ,重新获取)
        if min_loc[0] > max_loc[0]:
            y = min_loc[0]
        else:
            y = max_loc[0]

        if min_loc[1] > max_loc[1]:
            x = max_loc[1]
        else:
            x = min_loc[1]

        # x取最小值(如果x<10，取最大值）
        if x < 20:
            if min_loc[1] > max_loc[1]:
                x = min_loc[1]
            else:
                x = max_loc[1]

        # 这里就是下图中的绿色框框  50*50是移动块的大小
        cv2_tools.rectangle('bg.png', (y, x), (y + 50, x + 50), (7, 249, 151), 2)
        print('x坐标为：%d' % x)
        print('y坐标为：%d' % y)
        if y > 200:
            #定位到换一张
            elem = driver.find_element(By.CLASS_NAME, "JDJRV-slide-refresh").click()

            time.sleep(1)
            bkg, blk = get_image(driver)
            y, tp = get_distance(bkg, blk)
        return y, tp

distance, temp = get_distance(bkg, blk)
# 这个是用来模拟人为拖动滑块行为，快到缺口位置时，减缓拖动的速度，服务器就是根据这个来判断是否是人为登录的。
def get_tracks(dis):
    v = 0
    m = 0.3
    # 保存0.3内的位移
    tracks = []
    current = 0
    mid = distance*4/5
    while current <= dis:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0*m+0.5*a*(m**2)
        current += s
        tracks.append(round(s))
        v = v0+a*m
    return tracks
distance = int(278*108.11)
tracks = get_tracks(distance)

tracks.append(-(sum(tracks)-distance))
#获取滑动块的位置
slider = driver.find_element(By.CLASS_NAME, "JDJRV-slide-inner")
#模拟人为拖动滑块
ActionChains(driver).click_and_hold(slider).perform()
for track in tracks:
    ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
time.sleep(0.5)
ActionChains(driver).release().perform()
time.sleep(2)
#获取登录后的cookies
cookies = driver.get_cookies()
print(cookies)

#点击登录
driver.find_element(By.CLASS_NAME, "btn-img").click()
# #点击登陆
# driver.find_element(By.LINK_TEXT, "登录").click()
