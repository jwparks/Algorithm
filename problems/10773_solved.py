import sys
K = int(sys.stdin.readline())

nums = []
for _ in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        nums.pop(-1)
    else:
        nums.append(N)
print(sum(nums))