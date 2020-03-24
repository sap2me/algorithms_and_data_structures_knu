from tools import binary_continuous

def func(x):
    return x ** 3 + 4 * x ** 2 + x - 6

res = binary_continuous(func, 0, 0, 2)
print(res)