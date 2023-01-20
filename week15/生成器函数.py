# @Time: 2022/11/26 1:48
# @Author: 李树斌
# @File : 生成器函数.py
# @Software :PyCharm

# # 生成器函数
# def my_range(start, end, step):
#     while start < end:
#         yield start
#         start += step
#
# # 生成器函数的调用
# for i in my_range(1, 100, 1):
#     print(i)

#异步函数协程
import asyncio
async def my_range(start, end, step):
    while start < end:
        yield start
        start += step

# 生成器函数的调用
async def main():
    async for i in my_range(1, 100, 1):
        print(i)
# print(asyncio.run(main()))


async def async_function():
    return 1


try:
    print(asyncio.run(async_function()))
except RuntimeError as e:
    print(e)