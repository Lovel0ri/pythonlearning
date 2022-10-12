# @Time: 2022/10/12 15:48
# @Author: 李树斌
# @File : Bird.py
# @Software :PyCharm
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No,thanks")

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.song = 'Lalalala'

    def sing(self):
        print(self.song)

