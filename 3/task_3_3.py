from tools import binary_continuous

def func(x):
    return x ** 3 + x + 1

res = binary_continuous(func, 5, 0, 10)
print(res)