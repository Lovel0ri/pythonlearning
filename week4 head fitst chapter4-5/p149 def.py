# @Time: 2022/9/11 19:44
# @Author: 李树斌
# @File : p149 def.py
# @Software :PyCharm

vowels = set('aeiou')
word = input("Provide a word to search for vowels:")
fonud = vowels.intersection(set(word))
for vowel in fonud:
    print(vowel)