# @Time: 2022/11/26 2:02
# @Author: 李树斌
# @File : 买土豆.py
# @Software :PyCharm
import asyncio
import random

class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos
class Tomato:
    @classmethod
    def make(cls, num, *args, **kws):
        tomatos = []
        for i in range(num):
            tomatos.append(cls.__new__(cls, *args, **kws))
        return tomatos

all_potatos = Potato.make(5)
all_totatos = Tomato.make(5)
async def ask_for_potato():
    """协程函数"""
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))
async def ask_for_tomato():
    """协程函数"""
    await asyncio.sleep(random.random())
    all_totatos.extend(Tomato.make(random.randint(1, 10)))

async def take_tomatos(num):
    """协程函数"""
    count = 0
    while True:
        if len(all_totatos) == 0:
            await ask_for_tomato()
        tomato = all_totatos.pop()
        yield tomato
        count += 1
        if count == num:
            break
async def take_potatos(num):
    """协程函数"""
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break

async def buy_tomatos():
    bucket = []
    async for p in take_tomatos(50):
        bucket.append(p)
        print(f'Got tomato {id(p)}...')

async def buy_potatos():
    bucket = []
    async for p in take_potatos(50):
        bucket.append(p)
        print(f'Got potato {id(p)}...')

def main():
    import asyncio
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
    loop.close()

print(main())