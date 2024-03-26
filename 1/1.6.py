def Merge(arr, l1, r1, l2, r2):
    inv_count = 0
    result = []
    it1, it2 = 0, 0
    while (l1 + it1 <= r1 and l2 + it2 <= r2):
        if (arr[l1 + it1] < arr[l2 + it2]):
            result.append(arr[l1 + it1])
            it1 += 1
        else:
            result.append(arr[l2 + it2])
            it2 += 1
            inv_count += r1 - l1 - it1 + 1
    while (l1 + it1 <= r1):
        result.append(arr[l1 + it1])
        it1 += 1
    while (l2 + it2 <= r2):
        result.append(arr[l2 + it2])
        it2 += 1
    for i in range(r2 - l1 + 1):
        arr[l1 + i] = result[i]
    return inv_count

def MergeSort(arr, l, r):
    inv_count = 0
    if (l == r):
        return 0
    mid = (l + r) // 2
    inv_count += MergeSort(arr, l, mid)
    inv_count += MergeSort(arr, mid + 1, r)
    inv_count += Merge(arr, l, mid, mid + 1, r)
    return inv_count

n = int(input())

arr = list(map(int, input().split()))

inv_count = MergeSort(arr, 0, n - 1)

print(inv_count)

for i in arr:
    print(i, end=' ')