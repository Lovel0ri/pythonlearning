# @Time: 2022/10/5 18:43
# @Author: 李树斌
# @File : 6.4.5分配参数.py
# @Software :PyCharm
def story(**kwds):
    return "Once upon a time,there was a {job}'s called {name}.".format_map(kwds)
print(story(job='king', name='Gumby'))
params = {'job': 'language', 'name': 'Python'}

def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)

# print(power(2, 3, 4, 5))

# print(story(**params))#**params表示将params字典中的键值对分别作为关键字参数传递给format_map()函数

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None: # If stop is not provided
        start, stop = 0, start # Assume start is zero
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(interval(10))
print(interval(2, 5))