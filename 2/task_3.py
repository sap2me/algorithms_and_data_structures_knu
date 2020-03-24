def binary_search_left(a, x):
	lo = 0
	hi = len(a)
	while lo < hi:
		mid = (lo+hi)//2
		if a[mid] < x: lo = mid+1
		else: hi = mid
	return lo

def binary_search_right(a, x):
	lo = 0
	hi = len(a)
	while lo < hi:
		mid = (lo+hi)//2
		if x < a[mid]: hi = mid
		else: lo = mid+1
	return lo

n = int(input())
colors = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

for i in range(m):
    find_left = binary_search_left(colors, request[i])
    find_right = binary_search_right(colors, request[i])
    print(find_right - find_left)