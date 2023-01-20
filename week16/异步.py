# @Time: 2022/12/9 23:21
# @Author: 李树斌
# @File : 异步.py
# @Software :PyCharm

import asyncio


async def hello():
    print('Hello ...')

async def world():
    print('... World!')

async def main():
    await asyncio.gather(world(),hello() )

asyncio.run(main())