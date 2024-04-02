def find_kth_number(n, k):
    left = 1
    right = n * n

    while left < right:
        mid = (left + right) // 2
        count = 0

        for i in range(1, n + 1):
            count += min(mid // i, n)

        if count < k:
            left = mid + 1
        else:
            right = mid

    return right

n, k = map(int, input().split())

print(find_kth_number(n, k))