A, B = map(float, input().split())
c = 299792458
v = (A+B)/(1+(A*B)/(c**2))
print(v)