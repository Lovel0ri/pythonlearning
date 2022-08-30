# @Time : 2022/8/30  22:24
# @Author: 李树斌
# @File : 在列表中存储列表.py
# @Software : PyCharm

movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


#输出Eric Idle
print(f"单独输出Eric Idle")
print(movies[4][1][3])

#打印内外列表
print("打印内外列表")
for each_item in movies:
    print(each_item)