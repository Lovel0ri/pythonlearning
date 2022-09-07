# @Time: 2022/9/8 0:11
# @Author: 李树斌
# @File : 8.2传递实参.py
# @Software :PyCharm

def describe_pet(animal_type,pet_name):
    print(f"\n我有一只{animal_type}")
    print(f"他的名字是{pet_name}")

describe_pet("柴犬","啊旺")
describe_pet("柯基","啊基")

describe_pet(pet_name="小米",animal_type="仓鼠")#关键字实参