import sys

N = int(sys.stdin.readline())
NS = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MS = list(map(int, sys.stdin.readline().split()))
NS.sort()
for m in MS:
    start_idx = 0
    end_idx = N - 1
    while True:
        if (end_idx - start_idx) < 1:
            print(0)
            break
        mid_idx = (end_idx - start_idx)//2
        if m == NS[end_idx] or m == NS[start_idx] or m == NS[mid_idx]:
            print(1)
            break
        elif m > NS[mid_idx]:
            end_idx = mid_idx
        elif m < NS[mid_idx]:
            start_idx = mid_idx