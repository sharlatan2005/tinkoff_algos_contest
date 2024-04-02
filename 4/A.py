import sys

n = int(input())
arr = list(map(int, input().split()))

pr_arr = [0] * (n + 1)
xor_arr = [0] * (n + 1)

for i in range(1, n + 1):
    pr_arr[i] = pr_arr[i - 1] + arr[i - 1]
    xor_arr[i] = xor_arr[i - 1] ^ arr[i - 1]

k = int(input())

s = []
for _ in range(k):
    cmd, l, r = map(int, sys.stdin.readline().split())
    if cmd == 1:
        ans = pr_arr[r] - pr_arr[l - 1]
    elif cmd == 2:
        ans = xor_arr[r] ^ xor_arr[l - 1]
    s.append(str(ans))

print('\n'.join(s))