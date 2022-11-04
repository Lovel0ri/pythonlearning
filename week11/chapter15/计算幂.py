# @Time: 2022/11/4 20:55
# @Author: 李树斌
# @File : 计算幂.py
# @Software :PyCharm
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '你好'

if __name__ == '__main__':
    app.run(debug=True)