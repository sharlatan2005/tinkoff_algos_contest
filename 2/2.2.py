from collections import deque

def find_minimums(N, K, sequence):
    window = deque()
    results = []
    
    for i in range(N):
        if window and window[0] <= i - K:
            window.popleft()
        
        while window and sequence[i] <= sequence[window[-1]]:
            window.pop()
        window.append(i)
        
        if i >= K - 1:
            results.append(sequence[window[0]])
    
    return results

N, K = map(int, input().split())
sequence = list(map(int, input().split()))

minimums = find_minimums(N, K, sequence)
print(*minimums)