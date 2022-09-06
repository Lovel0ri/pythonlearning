# @Time: 2022/9/6 19:51
# @Author: 李树斌
# @File : 7.2while循环.py
# @Software :PyCharm

# current_number = 1
# while current_number <=5:
#     print(current_number)
#     current_number+=1#current_number = current number +1


prompt = "I will repeat to you "
prompt+= "\nTell me ,what would you say to me "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

