K, N = map(int, input().split())
k_length = []
for k in range(K):
    k_length.append(int(input()))

start_length = 0
end_length = max(k_length)
if k_length.count(end_length) == N:
    print(end_length)
else:
    while True:
        if (end_length - start_length) <= 1:
            print(start_length)
            break
        mid_length = start_length+(end_length-start_length)//2
        count = 0
        for k in k_length:
            count += k//mid_length
        if count < N:
            end_length = mid_length
        elif count >= N:
            start_length = mid_length
