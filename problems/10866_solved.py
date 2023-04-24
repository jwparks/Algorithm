import sys
from collections import deque

def deque_cmd(deq: deque, cmd):
    cmd = cmd.split()
    if cmd[0] == 'push_front':
        X = int(cmd[1])
        deq.appendleft(X)
    elif cmd[0] == 'push_back':
        X = int(cmd[1])
        deq.append(X)
    elif cmd[0] == 'pop_front':
        print(deq.popleft()) if len(deq)>0 else print(-1)
    elif cmd[0] == 'pop_back':
        print(deq.pop()) if len(deq)>0 else print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        print(1) if len(deq)==0 else print(0)
    elif cmd[0] == 'front':
        print(deq[0]) if len(deq)>0 else print(-1)
    elif cmd[0] == 'back':
        print(deq[-1]) if len(deq)>0 else print(-1)


N = int(sys.stdin.readline())
deq = deque()
for _ in range(N):
    cmd = sys.stdin.readline()
    deque_cmd(deq, cmd)
