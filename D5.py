import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_apt = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_apt

size = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

def Solve():
    global size
    list_size = []
    sys.setrecursionlimit(N*N)
    for r in range(1, N+1):
        for c in range(1, N+1):
            if map_apt[r][c] == 0:
                continue
            # size = 0
            # Flood_Fill_DFS(r, c)
            size = Flood_Fill_BFS(r, c)
            list_size.append(size)
    list_size.sort()
    return list_size


def Flood_Fill_DFS(r, c):
    global size
    size += 1
    map_apt[r][c] = 0
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if map_apt[nr][nc] == 0:
            continue
        Flood_Fill_DFS(nr, nc)


def Flood_Fill_BFS(r, c):
    q = deque()
    q.append((r, c))
    map_apt[r][c] = 0
    ret = 1

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if map_apt[nr][nc] == 0:
                continue
            map_apt[nr][nc] = 0
            q.append((nr, nc))
            ret += 1
    
    return ret

N, map_apt = Input_Data()
sol = Solve()
print(len(sol))
print(*sol, sep='\n')

