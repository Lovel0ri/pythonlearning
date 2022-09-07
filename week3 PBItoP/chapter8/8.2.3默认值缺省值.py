# @Time: 2022/9/8 0:33
# @Author: 李树斌
# @File : 8.2.3默认值缺省值.py
# @Software :PyCharm

def describe_pet(pet_name,animal_type="狗"):
    print(f"\n我有一只{animal_type}")
    print(f"他的名字是{pet_name}")

describe_pet("旺财")
#TypeError: describe_pet() missing 1 required positional argument: 'animal_type'