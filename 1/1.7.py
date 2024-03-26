def prepare_killer(a, length):
    origidx = [None] * length
    for i in range(length):
        origidx[i] = i

    r = length - 1

    for l in range(r):
        p = (l + r) // 2
        origidx[l], origidx[p] = origidx[p], origidx[l]
    

    for i in range(length):
        a[origidx[i]] = i + 1

n = int(input())

a = [i + 1 for i in range(n)]

prepare_killer(a, n)

for i in a:
    print(i, end=' ')