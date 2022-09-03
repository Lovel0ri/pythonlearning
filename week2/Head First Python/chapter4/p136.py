# @Time: 2022/9/2 14:03
# @Author: 李树斌
# @File : p136.py
# @Software :PyCharm

import nesterbing
import pickle

new_man = []
try:
    with open('data_man.txt','rb') as man_file:
        new_man=pickle.load(man_file)
except IOError as err:
    print("File error:"+str(err))
except pickle.PickleError as perr:
    print("Pickle error"+str(perr))
nesterbing.print_lol(new_man)