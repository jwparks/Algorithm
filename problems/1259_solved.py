while True:
    N = int(input())
    if N == 0:
        break
    else:
        N_str = str(N)
        isRecurrent = True
        for i in range(len(N_str)):
            if N_str[i] != N_str[-(i+1)]:
                print('no')
                isRecurrent = False
                break
        if isRecurrent:
            print('yes')
