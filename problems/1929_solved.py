import sys

N_max = 1000000
isPrime = [False, False] + [True]*(N_max - 1)
for i in range(2, N_max + 1):
  if isPrime[i]:
    for j in range(2*i, N_max + 1, i):
        isPrime[j] = False

N, M = map(int, sys.stdin.readline().split())
for i in range(N, M+1):
    if isPrime[i]:
        print(i)