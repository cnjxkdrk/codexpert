import sys
from collections import deque


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	height = [int(readl()) for _ in range(N)]
	return N, height

# 입력받는 부분 
N, height = Input_Data()

# 여기서부터 작성
def Solve():
    sol_list = [0]*(N+1)
    stack = deque()
    for i, h in enumerate(height, 1):
        while stack and stack[-1][1] < h:
            sol_list[stack[-1][0]] = i
            stack.pop()
        stack.append((i, h))
    return sol_list[1:]

sol = Solve()

# 출력하는 부분
print(*sol, sep='\n')