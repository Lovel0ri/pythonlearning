# @Time: 2022/9/20 18:16
# @Author: 李树斌
# @File : settings.py
# @Software :PyCharm

class Settings:
    """存储游戏《外星人入侵中》所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (247,238,214)

        #飞船设置
        self.ship_speed = 1.5

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 2
        self.bullet_color = ( 0,0,0 )