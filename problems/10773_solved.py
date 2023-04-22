K = int(input())

nums = []
for _ in range(K):
    N = int(input())
    if N == 0:
        nums.pop(-1)
    else:
        nums.append(N)
print(sum(nums))