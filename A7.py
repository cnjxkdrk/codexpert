import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_cmd = [list(map(int, readl().split())) for _ in range(N)]
	return N, list_cmd


def Solve():
    q = deque()
    for cmd in list_cmd:
        if cmd[0] == 0:
            if q: print(q.popleft())
            else: print('E')
        elif cmd[0] == 1:
            q.append(cmd[1])
            pass
        elif cmd[0] == 2:
            print(len(q))


# 입력받는 부분
N, list_cmd = Input_Data()

Solve()