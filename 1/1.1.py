n, k = (int(i) for i in input().split())

arr = list(map(int, input().split()))

questions = list(map(int, input().split()))

def binarySearch(item, arr):
    l, r, mid = 0, len(arr) - 1, None

    while(l < r):
        mid = (l + r) // 2
        if (item < arr[mid]):
            r = mid
        elif (item > arr[mid]):
            l = mid + 1
        else:
            return True
    return arr[l] == item

for i in questions:
    if (binarySearch(i, arr)):
        print("YES")
    else:
        print("NO")