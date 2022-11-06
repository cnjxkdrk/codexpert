import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	return N

# 입력 받는 부분
N = Input_Data()

# 여기서부터 작성
def Solve():
    sol = []
    deck = deque()
    for i in range(N):
        deck.append(i+1)
    for i in range(N-1):
        cnt = deck[-1] // 2
        # for _ in range(cnt):
        #     deck.append(deck.popleft())
        deck.rotate(-cnt)
        sol.append(deck.popleft())
    sol.append(deck[-1])
    return sol

ans = Solve()
# 출력하는 부분
print(*ans)