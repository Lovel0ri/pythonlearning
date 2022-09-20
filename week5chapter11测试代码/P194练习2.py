# @Time: 2022/9/20 10:55
# @Author: 李树斌
# @File : P194练习2.py
# @Software :PyCharm

def get_city_country(city,country,population=''):
    if population:
        full_info = f'{city},{country} - {population}'
    else:
        full_info = f'{city},{country}'
    return full_info