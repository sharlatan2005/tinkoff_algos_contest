arr = list(map(int, input().split()))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def add_node(root, val):
    if root == None:
        return Node(val)
    if (val <= root.val):
        root.left = add_node(root.left, val)
    elif (val > root.val):
        root.right = add_node(root.right, val)
    return root

def print_tree(root):
    if (root.left != None):
        print_tree(root.left)
    if (root.right != None):
        print_tree(root.right)
    print(root.val)

root = Node(arr[0])

for item in arr[1:]:
    add_node(root, item)

print_tree(root)

