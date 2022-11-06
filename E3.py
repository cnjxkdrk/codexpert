from doctest import OutputChecker
import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_ch = [list(map(int, readl().split())) for _ in range(R)]
	return R, C, map_ch   


sol_hour, sol_last_cnt_ch = -1, -1
# 입력받는 부분
R, C, map_ch = Input_Data()
d = ((-1, 0), (1, 0), (0, -1), (0, 1))


# 여기서부터 작성
def BFS(r, c):
    q = deque()
    q.append((r, c))
    del_list = []
    chk = [[0]*C for _ in range(R)]
    chk[r][c] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if chk[nr][nc] == 1:
                continue
            if map_ch[nr][nc] == 1:
                del_list.append((nr, nc))
                chk[nr][nc] = 1
                continue
            q.append((nr, nc))
            chk[nr][nc] = 1
    
    return del_list

def Solve():
    time = 0
    cnt_ch = sum([1 for r in range(R) for c in range(C) if map_ch[r][c]==1])
    
    while cnt_ch > 0:
        del_list = BFS(0, 0)
        for r, c in del_list:
            map_ch[r][c] = 0
        cnt_ch -= len(del_list)
        time += 1

    return time, cnt_ch + len(del_list)

sol_hour, sol_last_cnt_ch = Solve()

# 출력하는 부분
print(sol_hour, sol_last_cnt_ch, sep='\n')

'''
** INPUT
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

** OUTPUT
3
5
'''