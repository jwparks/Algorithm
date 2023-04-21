N = int(input())
for i in range(N):
    R, S = input().split()
    R = int(R)
    print(''.join([''.join([s]*R) for s in S]))