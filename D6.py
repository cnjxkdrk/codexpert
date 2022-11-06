import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_town = [list(map(int, readl().strip())) for _ in range(N)]
    return N, map_town

def BFS(r, c):
    q = deque()
    q.append((r, c))
    map_town[r][c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if map_town[nr][nc] == 0:
                continue
            q.append((nr, nc))
            map_town[nr][nc] = 0

def Solve():
    num_lake = 0
    for r in range(N):
        for c in range(N):
            if map_town[r][c] == 0:
                continue
            num_lake += 1
            BFS(r, c)
    
    return num_lake



N, map_town = Input_Data()
d = ((-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1))

sol = Solve()
print(sol)