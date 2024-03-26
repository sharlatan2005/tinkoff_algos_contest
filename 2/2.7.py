from collections import deque
import sys 

q1 = deque()
q2 = deque()

n = int(sys.stdin.readline())

ans = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if (cmd[0] == "+"):
        q2.append(cmd[1])
        if (len(q1) < len(q2)):
            q1.append(q2.popleft())
    if (cmd[0] == "*"):
        if (len(q1) > len(q2)):
            q2.appendleft(cmd[1])
        elif (len(q1) == len(q2)):
            q1.append(cmd[1])
    elif (cmd[0] == "-"):
        if (len(q1) > len(q2)):
            ans.append(q1.popleft())
        elif (len(q1) == len(q2)):
            ans.append(q1.popleft())
            q1.append(q2.popleft())

print('\n'.join(map(str, ans)))