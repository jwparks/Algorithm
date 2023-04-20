def get_digitsum(n):
    sum = 0
    while n:
        sum, n = sum + n % 10, n // 10
    return sum

L, U = map(int, input().split())
sum = 0
for N in range(L, U+1):
    print(N)
    sum += get_digitsum(N)
print(sum)