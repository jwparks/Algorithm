import sys
N = int(sys.stdin.readline())

ys = {}
for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    try:
        ys[y].append(x)
    except:
        ys[y] = [x]

key_sort = list(ys.keys())
key_sort.sort()
for i in range(len(key_sort)):
    for j in sorted(ys[key_sort[i]]):
        print(j, key_sort[i])