n, k = (int(i) for i in input().split())

arr = list(map(int, input().split()))

questions = list(map(int, input().split()))

for q in questions:
    l = 0
    r = len(arr) - 1
    mid = None
    while (l < r):
        mid = (l + r) // 2
        if (arr[mid] < q):
            l = mid + 1
        elif (arr[mid] > q):
            r = mid 
        else:
            break
    targets = []
    if (arr[mid] == q):
        targets = [arr[mid]]
    elif (mid == 0):
        targets = [arr[mid], arr[mid + 1]]
    else:
        targets = [arr[mid - 1], arr[mid], arr[mid + 1]]
    print(sorted(targets, key=lambda x: abs(x - q))[0])


    