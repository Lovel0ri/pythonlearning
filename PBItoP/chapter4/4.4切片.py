# @Time: 2022/9/6 18:15
# @Author: 李树斌
# @File : 4.4切片.py
# @Software :PyCharm

# letter = ['A','B','C','D']
# print(letter[:3])
# print(letter[1:3])
# print(letter[-2:])

#4.4.2遍历切片
letters = ['A','B','C','D','E']
print("Here are some letters:")
for letter in letters:
    print(letter)

# print(letters)
# letter_r = letters[:]
# letter_r.reverse()
# print(letter_r)

letters = ['A','B','C','D','E']
letters.append('F')
print(letters)