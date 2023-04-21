A = int(input())
B = int(input())
C = int(input())

N = A*B*C
number_count = {}
for s in str(N):
    try:
        number_count[int(s)] += 1
    except:
        number_count[int(s)] = 1

for i in range(10):
    try:
        print(number_count[i])
    except:
        print(0)