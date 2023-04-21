N = 9
max_number = 0
max_idx = 0
for i in range(N):
    n = int(input())
    if n > max_number:
        max_number = n
        max_idx = i+1
print(max_number)
print(max_idx)
