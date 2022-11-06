import sys
import bisect

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos

def bs_lower(s, e, d):
    ret = -1
    while s<=e:
        m = (s+e)//2
        if pos[m] >= d:
            ret = m
            e = m-1
        else: s = m+1
    return ret

def bs_upper(s, e, d):
    ret = -1
    while s<=e:
        m = (s+e)//2
        if pos[m] <= d:
            ret = m
            s = m+1
        else: e = m-1
    return ret 

def Solve():
    ret = 0
    pos.sort()
    for i in range(N-2):
        for j in range(i+1, N-1):
            gap = pos[j] - pos[i]
            rs = pos[j] + gap
            re = pos[j] + 2*gap
            lower = bs_lower(0, N-1, rs)
            if lower == -1: continue
            upper = bs_upper(0, N-1, re)
            ret += (upper-lower+1)
    return ret 

def Solve_Bisect():
    ret = 0
    pos.sort()
    # 1 3 4 7 10
    for i in range(N-2):
        for j in range(i+1, N-1):
            gap = pos[j] - pos[i]
            # gap 이상 2*gap 이하
            lower = bisect.bisect_left(pos, pos[j] + gap)
            if lower == N or pos[lower] > pos[j] + 2*gap: continue
            upper = bisect.bisect_right(pos, pos[j] + 2*gap)
            ret += (upper-lower)
    return ret

sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
sol = Solve()
# sol = Solve_Bisect()

# 출력하는 부분
print(sol)