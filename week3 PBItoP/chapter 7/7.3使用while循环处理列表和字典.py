# @Time: 2022/9/6 22:25
# @Author: 李树斌
# @File : 7.3使用while循环处理列表和字典.py
# @Software :PyCharm

unconfirmed_users = ['A','B','C']
confirmed_users = []
#验证每个用户，知道没有未验证的用户
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user}")
    confirmed_users.append(current_user)

    #显示已经验证的用户
print(f"\n The following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())