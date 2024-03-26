from collections import deque

n = int(input())

balls = list(map(int, input().split()))

stack = deque()

ans = 0
i = 0
while (i < n):
    ball = balls[i]
    cnt = 0
    while (i < n and balls[i] == ball):
        stack.append(ball)
        i += 1
        cnt += 1
    if (cnt >= 3):
        for _ in range(cnt):
            stack.pop()
        ans += cnt
        break

while (i < n):
    ball = balls[i]
    while (i < n and balls[i] == ball):
        i += 1
        stack.append(ball)
    cnt = 0
    while (len(stack) > 0 and stack[-1] == ball):
        stack.pop()
        cnt += 1
    if (cnt >= 3):
        ans += cnt
    else:
        for _ in range(cnt):
            stack.append(ball)
print(ans)