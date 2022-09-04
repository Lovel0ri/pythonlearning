# @Time: 2022/9/4 17:20
# @Author: 李树斌
# @File : p88练习.py
# @Software :PyCharm

#6-1
bingbing = {'first name': 'bingbing',
            'last name': 'Chen',
            'age': 19,
            'City': 'Guangzhou'}
print(bingbing)

#6-2
peoplenumber = dict()

# peoplenames = {'bingbing', 'saojie', 'cingcing'}
peoplenumber["bingbing's number"] = 20
peoplenumber["saojie's number"] = 18
peoplenumber["cingcing's number"] = 20
print(peoplenumber)


print("bingbing's favorite is " + str(peoplenumber["bingbing's number"]))
print("saojie's number is " + str(peoplenumber["saojie's number"]))
print("cingcing's number is " + str(peoplenumber["cingcing's number"]))


