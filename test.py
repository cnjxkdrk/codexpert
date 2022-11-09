import sys

def Input_Data():
	N, K = map(int, readl().split())
	num = list(map(int, readl().split()))
	return N, K, num

def DFS(s, remain):
    if remain == 0:
        return True
    if remain < 0:
        return False

    for i in range(s, N):
        if DFS(i+1, remain-num[i]): return True

    return False




sol = []
# 입력 받는 부분
readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
	N, K, num = Input_Data()
	# 여기서부터 입력



# 출력하는 부분
print(*sol, sep = '\n')

# https://drive.google.com/open?id=1iiWjf-PKBq_nfD9lqKtuyU4bqEbUaq_5
