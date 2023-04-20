import itertools

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


L, U = map(int, input().split())
sum = 0
for N in range(L, U+1):
    prime_factor = []
    for p in prime_factors(N):
        prime_factor.append(p)
    unique_prime = set(prime_factor)
    sum_factors = 1
    for up in unique_prime:
        upc = prime_factor.count(up)
        sum_factors *= ((up**(upc+1)-1)/(up-1))
    sum += sum_factors
print(int(sum))