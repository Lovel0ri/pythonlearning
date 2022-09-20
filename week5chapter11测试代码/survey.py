# @Time: 2022/9/20 11:17
# @Author: 李树斌
# @File : survey.py
# @Software :PyCharm
class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """存储一个答案，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self,new_response):
        """存储单份问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print('Survey results:')
        response = [i for i in self.responses]
        print(f'- {response}')

# my_response = AnonymousSurvey('你喜欢上学吗')
# my_response.show_question()
# my_response.store_response('可能喜欢')
# my_response.show_results()