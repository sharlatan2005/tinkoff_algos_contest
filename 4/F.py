def merge_intervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    total_length = sum(end - start for start, end in merged)
    return total_length

n = int(input())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append([l, r])

merged_length = merge_intervals(segments)
print(merged_length)