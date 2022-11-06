import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_info = [readl().strip() for _ in range(R)]
    return R, C, map_info

def BFS(r, c, time):
    q = deque()
    q.append((r, c, 0))
    chk = [[0]*C for _ in range(R)]
    chk[r][c] = 1
    sol = 0

    while q:
        r, c, time = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if map_info[nr][nc] == 'W':
                continue
            if chk[nr][nc] > 0:
                continue
            ntime = time + 1
            q.append((nr, nc, ntime))
            chk[nr][nc] = ntime
            sol = max(sol, ntime)

    return sol


def Solve():
    sol = -1
    L_info = [(r, c) for r in range(R) for c in range(C) if map_info[r][c] == 'L']
    for r, c in L_info:
        sol = max(sol, BFS(r, c, 0))

    return sol



R, C, map_info = Input_Data()
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
# chk = [[0]*C for _ in range(R)]

sol = Solve()
print(sol)



# INPUT
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW

# OUTPUT
# 8