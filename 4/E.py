def check(x, pr_sum, k):
    l = 1
    r = 1
    cnt = 0
    while l < len(pr_sum):
        while r < len(pr_sum) and pr_sum[r] - pr_sum[l - 1] <= x:
            r += 1
        if r == l:
            return False
        l = r
        cnt += 1
    return cnt <= k
n, k = map(int, input().split())

numbers = list(map(int, input().split()))

pr_sum = [0] * (n + 1)

for i in range(1, n + 1):
    pr_sum[i] = pr_sum[i - 1] + numbers[i - 1]

l = 1
r = pr_sum[n]

for i in range(l, r + 1):
    print(check(i, pr_sum, k), end=' ')

# while r - l > 1:
#     mid = (l + r) // 2
#     if check(mid, pr_sum, k):
#         r = mid
#     else:
#         l = mid
if check(l, pr_sum, k) == check(r, pr_sum, k) == True:
    print(l)
else:
    print(r)