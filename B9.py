import sys
import bisect


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = [0] + list(map(int, readl().split()))
	T = int(readl())
	query = list(map(int, readl().split()))
	return N, num, T, query

def Solve():
    sol = []
    for q in query:
        start = bisect.bisect_left(num, q, lo=1)
        end = bisect.bisect_right(num, q, lo=1)

        if start != len(num) and num[start] == q:
            sol.append(end-start)
        else:
            sol.append(0)
    
    return sol    

# 입력받는 부분
N, num, T, query = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(*sol)