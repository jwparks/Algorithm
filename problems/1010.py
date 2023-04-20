T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    count = 1
    for n in range(N):
        count *= M
        for m in range(M):
            count *=(m-n)

