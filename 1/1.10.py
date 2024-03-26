# n = int(input())

def sum_col(i, n, m):
    return int((int((1 + m * (n - 1) + 1) / 2 * n) + int((i + m * (n - 1) + i) / 2 * n)) / 2 * i)

def sum_str(i, n, m):
    return int(((1 + i * m) / 2 * i * m))

def diff_sum_col(i, n, m):
    return sum_col(m, n, m) - sum_col(i, n, m) < sum_col(i, n, m)

def diff_sum_str(i, n, m):
    return sum_str(n, n, m) - sum_str(i, n, m) < sum_str(i, n, m)

def binary_search_col(n, m):
    l = 1
    r = m
    while (l + 1 != r):
        mid = (l + r) // 2
        if diff_sum_col(mid, n, m) == 0:
            l = mid
        else:
            r = mid
    if abs(sum_col(m, n, m) - sum_col(l, n, m) - sum_col(l, n, m)) < abs(sum_col(m, n, m) - sum_col(r, n, m) - sum_col(r, n, m)):
        return l
    else:
        return r

def binary_search_str(n, m):
    l = 1
    r = m
    while (l + 1 != r):
        mid = (l + r) // 2
        if diff_sum_str(mid, n, m) == 0:
            l = mid
        else:
            r = mid
    if abs(sum_str(m, n, m) - sum_str(l, n, m) - sum_str(l, n, m)) < abs(sum_str(m, n, m) - sum_str(r, n, m) - sum_str(r, n, m)):
        return l
    else:
        return r


g = int(input())
for _ in range(g):
    n, m = (int(i) for i in input().split())

    col_ind = binary_search_col(n, m)
    str_ind = binary_search_str(n, m)

    if abs(sum_str(m, n, m) - sum_str(str_ind, n, m) - sum_str(str_ind, n, m)) < abs(sum_col(m, n, m) - sum_col(col_ind, n, m) - sum_col(col_ind, n, m)):
        print("H", str_ind + 1)
    else:
        print("V", col_ind + 1)
