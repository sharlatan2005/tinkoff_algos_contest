def query(x1, y1, x2, y2, pref):
    return pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1]

n, m, k = map(int, input().split())

matr = []
for _ in range(n):
    stroka = list(map(int, input().split()))
    matr.append(stroka)

pref = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    pref[i][0] = pref[i - 1][0] + matr[i - 1][0]

for j in range(1, m + 1):
    pref[0][j] = pref[0][j - 1] + matr[0][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + matr[i - 1][j - 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(query(x1, y1, x2, y2, pref))
