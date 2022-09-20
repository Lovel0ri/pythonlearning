# @Time: 2022/9/20 12:14
# @Author: 李树斌
# @File : test_survey.py
# @Software :PyCharm
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey的测试"""
    def test_store_single_response(self):
        """测试单个答案是否会被妥善的存储"""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)

if __name__ == '__main__':
    unittest.main()