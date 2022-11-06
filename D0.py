import sys
 
def Input_Data():
    N, K = map(int, readl().split())
    num = list(map(int, readl().split()))
    return N, K, num
 
 
def DFS_Binary(n, remain):
    if remain == 0: return True
    if remain < 0: return False
    if n >= N: return False
 
    if DFS_Binary(n+1, remain-num[n]): return True
    if DFS_Binary(n+1, remain): return True
     
    return False
 
 
def DFS_Multi(s, remain):
    if remain == 0: return True
    if remain < 0: return False
 
    for n in range(s, N):
        if DFS_Multi(n+1, remain-num[n]): return True
     
    return False
 
 
sol = []
 
# 입력 받는 부분
readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
     
    # 여기서부터 입력
    ret = DFS_Binary(0, K) # 이진 선택 (중복 순열)
    # ret = DFS_Multi(0, K) # 조합 
     
    if ret: sol.append("YES")
    else: sol.append("NO")
 
 
# 출력하는 부분
print(*sol, sep = '\n')