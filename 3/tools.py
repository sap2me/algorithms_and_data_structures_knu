def binary_continuous(func, c, a, b):
    left = a
    right = b
    m = (left + right)/2.0

    while left != m and m != right:
        if func(m) <= c:
            left = m
        else:
            right = m
        m = (left + right)/2.0

    return left