# @Time: 2022/9/20 11:56
# @Author: 李树斌
# @File : 11.2.2language_survey.py
# @Software :PyCharm
from survey import AnonymousSurvey

"""定义一个问题，并创建一个程序"""
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

"""显示问题并存储答案"""
my_survey.show_question()
print('Enter q to quit')
while True:
    response = input('Language :')
    if response == 'q':
        break
    my_survey.store_response(response)


#显示调查结果
print('\n Thank you to participate in the survey!')
my_survey.show_results()