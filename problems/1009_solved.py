N = int(input())
#N = 1
for i in range(N):
    A, B = map(int, input().split())
    B_bin = '{0:b}'.format(B)
    B_bin = B_bin[::-1]
    B_decompose = []
    B_decompose_idx = []
    for b in range(len(B_bin)):
        B_decompose.append(2 ** (b * 2))
        if B_bin[b] == '1':
            B_decompose_idx.append(b)
    mod10_list = []
    for b in range(len(B_decompose)):
        if b == 0:
            mod10_list.append(A%10)
        else:
            mod10_list.append((mod10_list[-1]**2)%10)
    A_alt = 1
    for b in range(len(B_bin)):
        if B_bin[b] == '1':
            A_alt *= mod10_list[b]
    computer_idx = A_alt % 10
    print(10 if computer_idx==0 else computer_idx)
