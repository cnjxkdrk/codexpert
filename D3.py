import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
	return N, matrix

def DFS(n, city, sum_cost):
    global sol
    if sol <= sum_cost:
        return

    if n >= N:
        if matrix[city][1] and sol > sum_cost + matrix[city][1]:
            sol = sum_cost + matrix[city][1]
        return

    for i in range(2, N+1):
        if chk[i]:
            continue
        if matrix[city][i] == 0:
            continue
        chk[i] = True
        DFS(n+1, i, sum_cost + matrix[city][i])
        chk[i] = False



sol = 10000
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
chk = [False]*(N+1)
DFS(1, 1, 0)

# 출력하는 부분
print(sol)