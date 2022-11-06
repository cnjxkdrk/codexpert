import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_score = list(map(int, readl().split()))
	return N, list_score


sol = [-1, -1, -1]
# 입력받는 부분
N, list_score = Input_Data()

# 여기서부터 받는
arr = [(i, j) for i, j in enumerate(list_score, start=1)]
arr.sort(key=lambda x: (-x[1], x[0]))

for i in range(3):
    sol[i] = arr[i][0]

# 출력하는 부분
print(*sol)