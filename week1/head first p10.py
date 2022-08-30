# @Time : 2022/8/29  23:21
# @Author: 李树斌
# @File : head first p10.py
# @Software : PyCharm
name = ["A","B","C","D"]
print(f"这是被邀请去看电影的同学{name}")

print(f"目前有{len(name)}名同学被邀请去看电影")
#D同学没空去
name.pop()
print(f"但是D同学没空去，所以我们现在只有{name}去看电影")
#C同学邀请E同学一起来看电影
name.append("E")
print(f"然后C同学邀请了{name[3]}同学")
#弹出所有要去看电影的同学
print(f"现在我们有这些同学去看电影{name},人数是{len(name)}")
print("\n2小时候过后，他们从影院出来了")


#C同学不跟他们一起回家
print(f"{name[2]}同学:我自己回家啦，你们一起回去吧!")
#删掉C同学，弹出此时一起回家的同学的名字
del name[3]
print(f"现在只有{name}一起回家")
