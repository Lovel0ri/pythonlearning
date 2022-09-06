# @Time: 2022/9/4 17:47
# @Author: 李树斌
# @File : 6.3遍历字典.py
# @Software :PyCharm

# 6.3.1
# use_0 = {
#     'username' : 'efermi',
#     'first': 'enrico',
#     'last' : 'fermi',
# }
# for key,value in use_0.items():
#     print(f"\nKey:{key}  Value:{value}")

#6.3.2
favourite_languages = {
    'jen' : 'python',
    'sarah' : 'C',
    'edward' : 'ruby',
    'phil' : 'python'
}
names =' '.join([t for t in favourite_languages.keys()])
print(names)
# 输出结果是 jen sarah edward phil
for name in favourite_languages.keys():
    print(name.title())
#输出结果是
"""
Jen
Sarah
Edward
Phil
"""

for name,language in favourite_languages.items():
    print(f"{name.title()}'s favorite is {language.title()}")
