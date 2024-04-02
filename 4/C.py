n, k = map(int, input().split())

coords = list(map(int, input().split()))

def check(x, coords, k):
    cnt = 1
    cur_cow = coords[0]

    for coord in coords:
        if (coord - cur_cow >= x):
            cnt += 1
            cur_cow = coord
    
    return cnt >= k

l = 0
r = coords[-1] - coords[0] + 1

while r - l > 1:
    mid = (l + r) // 2
    if check(mid, coords, k):
        l = mid
    else:
        r = mid
    
print(l)