# @Time: 2022/9/20 0:14
# @Author: 李树斌
# @File : p187练习.py
# @Software :PyCharm
import json
filename = 'favnum.json'

#10-11 10 -12
def get_fav_num():
    try:
        with open(filename) as f:
            fav_num = json.load(f)
            print(f"你喜欢的数字是{fav_num}")
    except FileNotFoundError:
        return None
    else:
        return fav_num

def greet_user():
    fav_num = get_fav_num()
    if fav_num:
        print(f"您好，您喜欢的数字是{fav_num}")
    else:
        fav_num = input("请输入您喜欢的数字")
        with open(filename,'w') as f:
            json.dump(fav_num,f)
            print(f"下次我会记得你喜欢的数字的")
greet_user()
