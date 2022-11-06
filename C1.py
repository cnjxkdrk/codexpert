import sys
import bisect

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl()) 
    pos = list(map(int, readl().split()))
    M = int(readl())
    return N, pos, M

def Solve():
    sol = -1
    s = 0
    e = max(pos)
    while s<=e:
        m = (s+e)//2
        cost = sum([min(x, m) for x in pos])
        if cost == M:
            sol = m
            return sol
        elif cost < M:
            sol = m
            s = m+1
        else:
            e = m-1
    return sol

sol = -1
# 입력받는 부분
N, pos, M = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)