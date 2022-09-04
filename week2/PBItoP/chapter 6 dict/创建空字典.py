# @Time: 2022/9/4 16:27
# @Author: 李树斌
# @File : 创建空字典.py
# @Software :PyCharm

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
#
# #修改字典中的值
# alien_0['color'] = 'yellow'
# print(alien_0['color'])
alien_0 = {'x_position': 0 ,'y_position': 25, 'speed': 'medium'}
print(f"Original x_position : {alien_0['x_position']}")
print(alien_0)

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")
