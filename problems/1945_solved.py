import sys

N = int(sys.stdin.readline())
ratios = []
types = []
for _ in range(N):
    xbl, ybl, xtr, ytr = map(int, sys.stdin.readline().split())
    xtl, ytl, xbr, ybr = xbl, ytr, xtr, ybl
    # d1
    ratios.append(xtl / ytl)
    types.append(+1)
    # d2
    ratios.append(xbr / ybr)
    types.append(-1)
ds = sorted(zip(ratios, types), key=lambda x: (x[0], -x[1]))
count = 0
max_count = 0
for d, t in ds:
    count += t
    if count > max_count:
        max_count = count
print(max_count)

# 흠,.,,.,,
# import sys
# from math import gcd
#
# def LCM(x:list):
#     lcm = 1
#     for i in x:
#         lcm *= i // gcd(lcm, i)
#     return lcm
#
# N = int(sys.stdin.readline())
# TL_numers = []
# TL_denoms = []
# BR_numers = []
# BR_denoms = []
# for _ in range(N):
#     xbl, ybl, xtr, ytr = map(int, sys.stdin.readline().split())
#     xtl, ytl, xbr, ybr = xbl, ytr, xtr, ybl
#
#     TL_denom = gcd(xtl, ytl)
#     TL_numers.append(xtl // TL_denom)
#     TL_denoms.append(ytl // TL_denom)
#
#     BR_denom = gcd(xbr, ybr)
#     BR_numers.append(xbr // BR_denom)
#     BR_denoms.append(ybr // BR_denom)
#
# lcm = LCM(TL_denoms+BR_denoms)
# counter = {}
# for i in range(N):
#     TL_q = lcm//TL_denoms[i]
#     BR_q = lcm // BR_denoms[i]
#     for j in range(TL_numers[i]*TL_q, BR_numers[i]*BR_q+1):
#         try:
#             counter[j] += 1
#         except:
#             counter[j] = 1
# print(max(counter.values()))