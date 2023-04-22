import sys
N = int(sys.stdin.readline()) #이게 훨~~~씬 빠름
stack = []
start_num = 1
stdout = []
valid = True
for _ in range(N):
    n = int(sys.stdin.readline())
    while start_num <= n:
        stack.append(start_num)
        start_num += 1
        stdout.append('+')

    if stack[-1] == n:
        stack.pop()
        stdout.append('-')
    else:
        valid = False
        break
if valid:
    for s in stdout:
        print(s)
else:
    print('NO')