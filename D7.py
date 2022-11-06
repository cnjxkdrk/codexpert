import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pixel = [readl().strip() for _ in range(N)]
    return N, pixel

def BFS_Normal(r, c):
    color = pixel[r][c]
    q = deque()
    q.append((r, c))
    chk_normal[r][c] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if chk_normal[nr][nc]:
                continue
            if pixel[nr][nc] != color:
                continue
            q.append((nr, nc))
            chk_normal[nr][nc] = 1

def BFS_Odd(r, c):
    group = {'R': 0, 'G': 0, 'B': 1}
    color = pixel[r][c]
    q = deque()
    q.append((r, c))
    chk_odd[r][c] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if chk_odd[nr][nc]:
                continue
            if group[pixel[nr][nc]] != group[color]:
                continue
            q.append((nr, nc))
            chk_odd[nr][nc] = 1

    

def Solve():
    normal, odd = 0, 0
    
    for r in range(N):
        for c in range(N):
            if chk_normal[r][c]:
                continue
            BFS_Normal(r, c)
            normal += 1
            if chk_odd[r][c]:
                continue
            odd += 1
            BFS_Odd(r, c)

    return normal, odd


N, pixel = Input_Data()
chk_normal = [[0]*N for _ in range(N)]
chk_odd = [[0]*N for _ in range(N)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

normal, odd = Solve()
print(normal, odd)



# INPUT
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR

# OUTPUT
# 4 3