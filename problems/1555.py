N_max = 10000
isPrime = [False, False] + [True]*(N_max - 1)
for i in range(2, N_max + 1):
  if isPrime[i]:
    for j in range(2*i, N_max + 1, i):
        isPrime[j] = False

a = eval("1024 + 1024")
print(a)
#N = int(input())
#numbers = map(int, input().split())
#operators = ['+', '-', '*', '/', '(', ')']

numbers = [1, 2, 3, 4, 5, 6]
