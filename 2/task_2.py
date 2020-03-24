def binary_search(array, elem):
	left = 0
	right = len(array) - 1
	while left < right:
		middle = left + (right - left) // 2
		if elem > array[middle]:
			left = middle + 1
		else:
			right = middle
	return elem == array[left]

n = int(input())
n_ls = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for elem in m_list:
	is_exist = binary_search(n_ls, elem)
	if is_exist:
		print('YES')
	else:
		print('NO')
