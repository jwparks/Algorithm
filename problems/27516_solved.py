from math import gcd

X, Y = map(int, input().split())
N = int(input())
targets = []
coefs = {}
for n in range(N):
    x, y = map(int, input().split())
    x -= X
    y -= Y
    if x!=0 and y<0:
        x_squared = x*abs(x)
        #a = x_squared / y
        denom = abs(gcd(x_squared, y))
        a_new = (x_squared//denom, y//denom)
        if a_new not in coefs:
            coefs[a_new] = 1
        else:
            coefs[a_new] += 1
if len(coefs) > 0:
    print(max(coefs.values()))
else:
    print(0)