import sys

n = int(input())

def query(x):
    print(x)
    sys.stdout.flush()
    return input()

l, r = 1, n

while (l != r):
    mid = (l + r) // 2 + 1
    hint = query(mid)
    if (hint == "<"):
        r = mid - 1
    elif (hint == ">="):
        l = mid

print("! " + str(l))    