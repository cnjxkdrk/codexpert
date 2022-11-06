import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	job = list(map(int, readl().split()))
	return N, M, job

def Solve(N, M, job):
    completed = []
    q = deque()
    for i, prior in enumerate(job):
        q.append((i, prior))

    while q:
        cur = q.popleft()
        flag = False
        for doc in q:
            if cur[1] < doc[1]:
                q.append(cur)
                flag = True
                break
        if not flag:
            completed.append(cur[0])
    
    return completed.index(M) + 1
    


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    # 입력받는 부분
    N, M, job = Input_Data()

    # 여기서부터 작성
    sol.append(Solve(N, M, job))

# 출력하는 부분
print(*sol, sep='\n')