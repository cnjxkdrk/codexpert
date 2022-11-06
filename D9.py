import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    H = [int(readl()) for _ in range(N)]
    return N, H

def Solve():
    cnt = 0
    stack = deque()
    for h in H:
        while stack and stack[-1] <= h:
            stack.pop()
        cnt += len(stack)
        stack.append(h)

    return cnt


N, H = Input_Data()
sol = Solve()
print(sol)
