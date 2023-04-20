m1 = 1
u1 = 0
m2 = int(input())**2
u2 = -1

mr = (m1-m2)/(m1+m2)
mw_1 = 2*m1/(m1+m2)
mw_2 = 2*m2/(m1+m2)

collisions = 0
while True:
    if u1-u2 > 0: #collision btw A, B
        v1 = mr*u1 + mw_2*u2
        v2 = mw_1*u1 - mr*u2
        u1, u2 = v1, v2
        collisions += 1
    elif u1 < 0: #collision btw A, Wall
        u1 = -u1
        collisions += 1
    else:
        break
print(collisions)



