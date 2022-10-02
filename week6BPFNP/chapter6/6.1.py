# @Time: 2022/10/2 17:11
# @Author: 李树斌
# @File : 6.1.py
# @Software :PyCharm

def fib(n):
    """Print a Fibonacci series up to n."""
    # n = input('How many Fibonacci numbers do you want? ')
    n = int(n)
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

print(fib(10))
print(fib(20))
print(fib.__doc__)