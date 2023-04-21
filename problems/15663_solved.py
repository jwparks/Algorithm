from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
P = sorted(list(set(permutations(N_list, M))))
for p in P:
    print(' '.join(str(p_i) for p_i in p))
