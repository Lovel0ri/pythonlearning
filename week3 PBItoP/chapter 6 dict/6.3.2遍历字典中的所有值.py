# @Time: 2022/9/4 19:40
# @Author: 李树斌
# @File : 6.3.2遍历字典中的所有值.py
# @Software :PyCharm

favourite_languages = {
    'jen': 'python',
    'Sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
for names in favourite_languages.keys():
    print(names)
#默认遍历所有的键
for names in favourite_languages:
    print(names)
# print({favourite_languages.get('jen')})
friends = ['phil','Sarah']
for name in favourite_languages.keys():
    print(f"Hello,{name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()

        print(f"\t{name.title()}, I see you love {language}")

