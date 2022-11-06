import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	matrix = [[0] + list(map(int, readl().split())) if 1<=s<=N else [0] * (N+1) for s in range(0, N+1)]
	return N, M, matrix

def BFS():
    q = deque()
    min_time = [10000]*(N+1)
    prev = [0] * (N+1)
    # (station number, time)
    min_time[1] = 0
    q.append((1, 0))

    while q:
        num, time = q.popleft()
        if min_time[num] < time: continue
        
        for i in range(1, N+1):
            ntime = time + matrix[num][i]
            if ntime >= min_time[i]: continue
            q.append((i, ntime))
            min_time[i] = ntime
            prev[i] = num                
                
    return min_time[M], prev

def Get_Route():
    route = []
    n = M
    while n!=0:
        route.append(n)
        n = prev[n]
    route.reverse()
    return route
        

sol = -1
route = []
# 입력 받는 부분
N, M, matrix = Input_Data()

# 여기서부터 작성
sol, prev = BFS()
route = Get_Route()

# 출력하는 부분
print(sol)
print(*route)