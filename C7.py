import sys
from collections import deque


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv

def BFS():
    chk = [[1000]*(N+2) for _ in range(N+2)]
    q = deque()
    q.append((1, 1, map_uv[1][1]))

    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        r, c, uv = q.popleft()
        if uv > chk[r][c]: continue

        for dr, dc in d:
            nr, nc = r+dr, c+dc
            nuv = uv+map_uv[nr][nc]
            if not 1<=nr<=N: continue
            if not 1<=nc<=N: continue
            if nuv >= chk[nr][nc]: continue
            q.append((nr, nc, nuv))
            chk[nr][nc] = nuv
    
    return chk[N][N]


sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)