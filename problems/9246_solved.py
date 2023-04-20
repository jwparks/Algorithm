import math

def linspace(lo, hi, n):
    delta = float(hi - lo)/n
    return [lo + i*delta for i in range(n)]

def prob(r, sigma):
    f = math.exp(-((r**2)/(2*(sigma**2))))
    return f

BE, B, TRI, TRO, DRI, DRO = map(float, input().split())
sigma = float(input())
ex_r_base = ((1+20)*20/2)/20

value = 0
value += 50 * (prob(0, sigma) - prob(BE, sigma))
value += 25 * (prob(BE, sigma) - prob(B, sigma))
value += ex_r_base * (prob(B, sigma) - prob(TRI, sigma))
value += ex_r_base*3 * (prob(TRI, sigma) - prob(TRO, sigma))
value += ex_r_base * (prob(TRO, sigma) - prob(DRI, sigma))
value += ex_r_base*2 * (prob(DRI, sigma) - prob(DRO, sigma))
print(value)