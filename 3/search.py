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


def binary_search_first(array, elem):
	left = 0
	right = len(array) - 1
	while left <= right:
		middle = left + (right - left) // 2
		if elem > array[middle]:
			left = middle + 1
		elif elem < array[middle]:
			right = middle - 1
		else:
			return middle
	return None


if __name__ == '__main__':
	data = [1, 7, 11, 15, 15, 15, 66, 102, 442, 1006]

	# Binary search test.
	print(binary_search(data, 1007))
	# Binary search first test.
	print(binary_search_first(data, 1))