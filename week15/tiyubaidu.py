# @Time: 2022/11/26 2:36
# @Author: 李树斌
# @File : tiyubaidu.py
# @Software :PyCharm
from requests_html import HTMLSession
import asyncio
import time
import aiohttp
import json
urls = []
session = HTMLSession()
url = "https://tiyu.baidu.com/api/match/%E4%B8%96%E7%95%8C%E6%9D%AF/live/date/2022-11-{}/direction/after?from=self"
url2 = "https://tiyu.baidu.com/api/match/%E4%B8%96%E7%95%8C%E6%9D%AF/live/date/2022-12-{}/direction/after?from=self"
#异步生成19-18号的url
async def get_urls():
    for i in range(19, 29):
        urls.append(url.format(i))
        urls.append(url2.format(i))
    return urls

# #同步请求
# def get_html(url,url2):
#     start = time.time()
#     urls = get_urls()
#     print(urls)
#     for i in urls:
#         r = session.get(i)
#         #读取data中的list数据
#         data = r.json()
#         data = data['data'][0]
#         #将数据写入本地data文件夹中
#         with open("data/{}.json".format(data['time']), "w", encoding="utf-8") as f:
#             f.write(str(data))
#     print("写入成功")
#     print("耗时：", time.time() - start)
# get_html(url,url2)

async def get_html(url,url2):
    start = time.time()
    urls = await get_urls()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in urls:
            tasks.append(asyncio.create_task(fetch(session, i)))
        #根据tasks发起异步请求
        responses = await asyncio.gather(*tasks)
        for response in responses:
            #解析str类型的json数据
            #将数据转换为str类型
            data = str(response)
            data = json.loads(response)
            data = data['data'][0]
            print(data)

    print("写入成功")
    print("耗时：", time.time() - start)

#异步请求
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

#创建事件循环
loop = asyncio.get_event_loop()
#将异步函数注册到事件循环中
loop.run_until_complete(get_html(url,url2))








