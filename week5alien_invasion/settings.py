# @Time: 2022/9/20 18:16
# @Author: 李树斌
# @File : settings.py
# @Software :PyCharm

class Settings:
    """存储游戏《外星人入侵中》所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230,230,230)