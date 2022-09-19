# @Time: 2022/9/20 1:27
# @Author: 李树斌
# @File : name.py
# @Software :PyCharm
from name_function import get_formatted_name
print("Enter'q' at any time to quit")
while True:
    first = input('\nPlease enter your first name:')
    if first == 'q':
        break
    last = input('Please enter your last name')
    if last == 'q':
        break

    formatted_name = get_formatted_name()
    print(f"\tNeatly formatted name:{formatted_name}.")
