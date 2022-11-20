# @Time: 2022/11/13 21:48
# @Author: 李树斌
# @File : 字典推导的应用.py
# @Software :PyCharm
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}
# for i,j in DIAL_CODES:
#     print(i,j)
print(country_code)
tinydict = {'Name': 'Zara', 'Age': 7}
tinydict.update({'sex':'男'})