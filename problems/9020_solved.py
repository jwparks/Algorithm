N_max = 10000
isPrime = [False, False] + [True]*(N_max - 1)
for i in range(2, N_max + 1):
  if isPrime[i]:
    for j in range(2*i, N_max + 1, i):
        isPrime[j] = False

N = int(input())
for i in range(N):
    A = int(input())
    A_half = int(A/2)
    for j in range(A_half):
        B = A_half-j
        C = A_half+j
        if isPrime[B] and isPrime[C]:
            print(B,C)
            break

