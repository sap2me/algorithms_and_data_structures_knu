"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""

def bsearch_rightmost(array, x):
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] <= x:
            left = m + 1
        else:
            right = m

    return left - 1

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

def counter(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """

    if array[bsearch_rightmost(array,x)-1]!=x:
        return 0
    return bsearch_rightmost(array,x)-binary_search_first(array,x)+1


array = [1, 23, 33, 22, 55 , 1, 22]
print(counter(array, 1))