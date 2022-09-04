# @Time: 2022/9/4 1:54
# @Author: 李树斌
# @File : p180创建字典.py
# @Software :PyCharm

cleese = {}
palin = dict()
cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['acotr','comedian','writer','file producer']
palin = {'Name':'Michael Palin','Occupations': ['comedian','actor','writer','tv']}
print(palin['Name'])
print(cleese)
print(cleese['Occupations'][-1])

palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare,North Somerset, England"
print(palin)
print(cleese)