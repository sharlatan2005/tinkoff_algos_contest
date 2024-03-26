from collections import deque
import sys 

queue = deque()
stack = deque()
n = int(sys.stdin.readline())

ans = []
dct = {}
first, second = None, None
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))
    first = cmd[0]
    if (len(cmd) > 1):
        second = cmd[1]
    if (first == 1):
        dct[second] = len(queue)
        queue.append(second)
    elif (first == 2):
        queue.popleft()
        for item in queue:
            dct[item] -= 1
    elif (first == 3):
        queue.pop()
    elif (first == 4):
        ans.append(dct[second])
    elif (first == 5):
        ans.append(queue[0])

print('\n'.join(map(str, ans)))