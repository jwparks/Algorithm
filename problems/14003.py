from bisect import bisect_left as bl
N = int(input())
arr = list(map(int, input().split()))
buffer = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] > buffer[-1]:
        buffer.append(arr[i])
    else:
        idx = bl(buffer, arr[i])
        buffer[idx] = arr[i]
print(len(buffer))
print(' '.join([str(b) for b in buffer]))