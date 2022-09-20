# @Time: 2022/9/20 12:14
# @Author: 李树斌
# @File : test_survey.py
# @Software :PyCharm
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """用setUP创建实例"""
        """针对AnonymousSurvey的测试"""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Chinese']
    def test_store_single_response(self):
        """测试单个答案是否会被妥善的存储"""

        self.my_survey.store_response(self.responses[0])
        self.assertIn('English',self.my_survey.responses[0])
    def test_store_three_responses(self):
        """测试三个答案是否会被妥善存储"""
        question = 'What language did you first learn to speak?'
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()