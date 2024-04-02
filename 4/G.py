def get_seconds(h, m, s):
    return h * 3600 + m * 60 + s 

n = int(input())

SECONDS_A_DAY = 24 * 3600
timetable = [0] * (SECONDS_A_DAY + 1)
timetable[-1] = -1

for _ in range(n):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    seconds_start = get_seconds(h1, m1, s1)
    seconds_end = get_seconds(h2, m2, s2)
    # seconds_start = int(input())
    # seconds_end = int(input())

    diff = seconds_end - seconds_start

    if diff > 0:
        timetable[seconds_start] += 1
        timetable[seconds_end] -= 1
    else:
        if diff < 0:
            timetable[seconds_start] += 1
            timetable[seconds_end] -= 1
        timetable[0] += 1

# for i in timetable:
#     if i != 0:
#         print(i)

i = 0
cnt = 0
ans = 0
while i < SECONDS_A_DAY:
    l = i
    r = i + 1
    cnt += timetable[i]
    # if cnt == n:
    #     print("start", i)
    while cnt == n and r < SECONDS_A_DAY + 1:
        cnt += timetable[r]
        r += 1
        # print(r)
    ans += r - l - 1
    i = r

print(ans)


