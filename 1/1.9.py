n = int(input())

arr = list(map(int, input().split()))
tr_arr = [0] * n
rb = n
ans = 1
print(ans, end=' ')

for idx in arr:
    idx -= 1
    tr_arr[idx] = 1
    if (idx + 1 == rb):
        rb = idx
        while(rb - 1 >= 0 and tr_arr[rb - 1] == 1):
            rb -= 1
            ans -= 1
    else:
        ans += 1
    print(ans, end=' ')
