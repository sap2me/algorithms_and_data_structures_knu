eps = 0.00000001

def func(x):
	return x ** 2 + x ** (1 / 2)

c_value = float(input())

left = 0
right = c_value
while right - left > eps:
	middle = left + right / 2
	y = func(middle)
	if y > c_value:
		right = middle
	else:
		left = middle

print(left)