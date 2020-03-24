from math import sin

from tools import binary_continuous


def func(x):
    return x / sin(x)

res = binary_continuous(func, 3, 1.6, 3)
print(res)