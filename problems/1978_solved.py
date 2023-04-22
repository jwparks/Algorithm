import sys

N_max = 1000
isPrime = [False, False] + [True]*(N_max - 1)
for i in range(2, N_max + 1):
  if isPrime[i]:
    for j in range(2*i, N_max + 1, i):
        isPrime[j] = False

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
counter = 0
for n in numbers:
    if isPrime[n]:
        counter += 1
print(counter)