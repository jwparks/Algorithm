N, M = map(int, input().split())
GT = []
for i in range(8):
    x = True if i%2==0 else False
    GT.append([x if j%2 == 0 else not x for j in range(8)])
#print(GT)

checkerboard = []
for n in range(N):
    line = input()
    checkerboard.append([True if l=='W' else False for l in line])
#print(checkerboard)

count = []
for n in range(N-8+1):
    for m in range(M-8+1):
        True_count = 0
        False_count = 0
        for i, ii in enumerate(range(n, n+8)):
            for j, jj in enumerate(range(m, m+8)):
                if checkerboard[ii][jj] == GT[i][j]:
                    True_count += 1
                else:
                    False_count += 1
        count.append(max([True_count, False_count]))
print(64-max(count))