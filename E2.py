import sys

def Input_Data():
    readl = sys.stdin.readline
    score = map(int, readl().split())
    ret = [[next(score) for _ in range(3)] for t in range(6)]
    return ret

def Get_Match_Info():
    arr = []
    for i in range(5):
        for j in range(i+1, 6):
            arr.append((i, j))
    return arr

def Chk(result):
    ret = all([sum(r) == 5 for r in result])
    return ret

def DFS(n, result):
    if n>=15:
        return 1

    t1, t2 = match_info[n]
    for i in range(3):
        if result[t1][i] and result[t2][2-i]:
            result[t1][i] -= 1
            result[t2][2-i] -= 1
            if DFS(n+1, result): return 1
            result[t1][i] += 1
            result[t2][2-i] += 1
    
    return 0

match_info = Get_Match_Info()
sol = []

for _ in range(4):
    score = Input_Data()
    sol.append(DFS(0, score) if Chk(score) else 0)

print(*sol)


# INPUT
# 5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
# 4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
# 5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
# 5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4

# OUTPUT
# 1 1 0 0