import sys
from collections import deque

n_cases = int(sys.stdin.readline())
for _ in range(n_cases):
    N, M = map(int, sys.stdin.readline().split())
    importance = deque(map(int, sys.stdin.readline().split()))
    sequence = deque([i for i in range(N)])
    count = 0
    while True:
        max_idx = importance.index(max(importance))
        importance.rotate(-max_idx)
        sequence.rotate(-max_idx)
        importance.popleft()
        out = sequence.popleft()
        count += 1
        if out == M:
            print(count)
            break
