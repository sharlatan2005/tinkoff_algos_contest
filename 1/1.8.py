n = int(input())
arr = sorted([i for i in input().rstrip()])

ans = []
left = []

i = 0
while(i < n):
    ch = arr[i]
    counter = 0
    while (i < len(arr) and arr[i] == ch):
        counter += 1
        i += 1
    if (counter % 2 != 0):
        left.append(arr[i - 1])
    if (counter > 1):
        counter -= counter % 2
        new_arr = [j for j in (arr[i - 1] * counter)]
        mid = (len(ans) - 1) // 2
        ans = ans[:(mid + 1)] + new_arr + ans[(mid + 1):]

if (len(left) > 0):
    mid = (len(ans) - 1) // 2
    ans = ans[:(mid + 1)] + [left[0]] + ans[(mid + 1):] 

pal = ""

for i in ans:
    pal += i
print(pal)

