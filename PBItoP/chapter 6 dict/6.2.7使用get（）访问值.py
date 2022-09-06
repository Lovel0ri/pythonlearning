# @Time: 2022/9/4 17:10
# @Author: 李树斌
# @File : 6.2.7使用get（）访问值.py
# @Software :PyCharm
alien_0 = {'color':'green', 'speed': 'slow'}
#获取不存在的值
# print(alien_0['points'])
#显示键值错误
#get 第一个参数用于指定键，这是必不可少的，第二个参数为指定键不存在时，要返回的值
point_value = alien_0.get('points','No point value assigned')
print(point_value)