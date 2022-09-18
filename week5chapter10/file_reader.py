# @Time: 2022/9/18 23:36
# @Author: 李树斌
# @File : file_reader.py
# @Software :PyCharm

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.strip())

filename = 'pi_million_digits.txt'
with open(filename) as file_project:
    lines = file_project.readlines()

pi_string = ''
for line in lines:
    pi_string +=line.strip()
print(f"{pi_string[:51]}...")
print(len(pi_string))
print(len(pi_string[:50]))