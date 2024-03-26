from collections import deque

n = int(input())

wagons = list(map(int, input().split()))

path2 = deque()   
tupik = deque()

i = 0
current_wagon = 1
actions = []
while (i < n):
    cnt1 = 0
    while (i < n and wagons[i] != current_wagon):
        tupik.append(wagons[i])
        cnt1 += 1
        i += 1
    if (i < n):
        actions.append((1, cnt1 + 1))
        tupik.append(wagons[i])
        i += 1
    cnt2 = 0
    while(len(tupik) > 0 and tupik[-1] == current_wagon):
        cnt2 += 1
        tupik.pop()
        current_wagon += 1
    actions.append((2, cnt2))

if (len(tupik) > 0):
    print(0)
else:
    output = str(len(actions)) + "\n"
    for action in actions:
        output += str(action[0]) + " " + str(action[1]) + "\n"
    print(output.rstrip())