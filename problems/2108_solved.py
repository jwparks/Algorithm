import sys


def return_key(dic):
    values = list(dic.values())
    keys = list(dic.keys())
    max_value = max(values)
    keys_return = []
    for v, value in enumerate(values):
        if value == max_value:
            keys_return.append(keys[v])
    if len(keys_return) > 1:
        keys_return.sort()
        return keys_return[1]
    else:
        return keys_return[0]

N = int(sys.stdin.readline())

mean = 0
median = []
freq = {}
for _ in range(N):
    M = int(sys.stdin.readline())
    median.append(M)
    mean += M
    try:
        if M > max_int:
            max_int = M
    except:
        max_int = M
    try:
        if M < min_int:
            min_int = M
    except:
        min_int = M
    try:
        freq[M] += 1
    except:
        freq[M] = 1
median.sort()
print(round(mean/N))
print(median[int((N-1)/2)])
print(return_key(freq))
print(abs(max_int - min_int))
