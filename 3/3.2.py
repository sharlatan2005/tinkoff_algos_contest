def get_height(root, tree):
    if (root == -1):
        return -1
    else:
        return max(get_height(tree[root][0], tree), get_height(tree[root][1], tree)) + 1

def is_binary_search_tree(node, tree):
    if node == -1:
        return True

    if tree[node][0] != -1 and tree[node][0] >= node:
        return False

    if tree[node][1] != -1 and tree[node][1] <= node:
        return False

    return (
        is_binary_search_tree(tree[node][0], tree) and
        is_binary_search_tree(tree[node][1], tree)
    )

def is_avl(root, tree):
    if root == -1:
        return True
    left = tree[root][0]
    right = tree[root][1]
    return is_avl(left, tree) and is_avl(right, tree) and abs(get_height(left, tree) - get_height(right, tree)) <= 1 and is_binary_search_tree(root, tree)



n, r = map(int, input().split())

tree = [[] for _ in range(n)]
for i in range(n):
    left, right = map(int, input().split())
    tree[i].append(left)
    tree[i].append(right)
    
print(int(is_avl(r, tree)))