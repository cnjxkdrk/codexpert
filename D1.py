from re import S
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0] * (N+1)  for n in range(N+1)]
	return N, matrix


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
def Solve():
    pass

def DFS(n, sum_cost):
    global min_cost
    if sum_cost >= min_cost:
        return

    if n >= N:
        if sum_cost < min_cost:
            min_cost = sum_cost
        return

    for c in range(1, N+1):
        if sel[c]:
            continue
        sel[c] = True
        DFS(n+1, sum_cost + matrix[n+1][c])
        sel[c] = False
    return


min_cost = 1000
sel = [False] * (N+1)
DFS(0, 0)
sol = min_cost
# 출력하는 부분
print(sol)