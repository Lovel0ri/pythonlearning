# @Time: 2022/9/2 13:25
# @Author: 李树斌
# @File : 调用pickle库.py
# @Software :PyCharm

import pickle
#用dunmp保存，用load回复
with open("mydata.pickle",'wb') as mysavedata:
    pickle.dump([1,2,'three'],mysavedata)
with open("mydata.pickle",'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)
print(a_list)
