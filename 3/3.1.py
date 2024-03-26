import sys
sys.setrecursionlimit(10**9)

def dfs(node, tree, visited, depth):
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            depth[child] = (depth[node][0] + 1, child)
            dfs(child, tree, visited, depth)

n = int(input())

nodes = list(map(int, input().split()))

tree = [[] for _ in range(n)] # списки смежности

for i in range(n - 1): # проходимся по nodes
    tree[nodes[i]].append(i + 1)
    tree[i + 1].append(nodes[i])

visited = [False] * n
depth = [(0, 0)] * n # массив глубин и индексов

dfs(0, tree, visited, depth)

the_deepest = max(depth, key=lambda x : x[0]) # кортеж (самая большая глубина, ее индекс)
height = the_deepest[0]

original_depth = [i[0] for i in depth] # массив глубин для ответа запоминаем

depth = [(0, 0)] * n # высчитываем глубины заново, начиная с самой глубокой вершины
visited = [False] * n

dfs(the_deepest[1], tree, visited, depth)

diam = max(depth, key=lambda x : x[0])[0]

print(height, diam)
print(*original_depth)