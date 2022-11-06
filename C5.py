import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	M, N = map(int, readl().split())
	map_box = [list(map(int, readl().split())) for _ in range(N)]
	return M, N, map_box

def BFS():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_box[i][j] == 0:
                cnt += 1
    if cnt==0: return 0
    
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(N):
        for j in range(M):
            if map_box[i][j] == 1:
                q.append((i, j, 0))

    while q:
        r, c, day = q.popleft()
        for dr, dc in d:
            nr, nc, nd = r+dr, c+dc, day+1
            if not 0<=nr<=N-1: continue
            if not 0<=nc<=M-1: continue
            if map_box[nr][nc] != 0: continue
            map_box[nr][nc] = 1
            cnt -= 1
            if cnt==0: return nd
            q.append((nr, nc, nd))

    return -1


sol = -1
# 입력 받는 부분
M, N, map_box = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)