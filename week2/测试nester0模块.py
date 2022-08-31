# @Time : 2022/8/31  17:40
# @Author: 李树斌
# @File : 测试nester0模块.py
# @Software : PyCharm

#暂时有bug没修复，无法调用nester1(已修复）
import nester1
movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
nester1.print_lol(movies,0)