import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    h, w = map(int, readl().split())
    r, c, s, k = map(int, readl().split())
    return h, w, r-1, c-1, s-1, k-1

def BFS():
    graph = [[0]*W for _ in range(H)]
    
    q = deque()
    q.append((R, C, 0))
    graph[R][C] = 1

    dh = [-1, -2, -2, -1, 1, 2, 2, 1]
    dw = [-2, -1, 1, 2, -2, -1, 1, 2]
    while q:
        ch, cw, cd = q.popleft()
        
        for i in range(8):
            nh, nw, nd = ch + dh[i], cw + dw[i], cd + 1
            if nh<0 or nh>=H or nw<0 or nw>=W: continue
            if graph[nh][nw] == 1: continue
            if nh==S and nw==K: return nd
            q.append((nh, nw, nd))
            graph[nh][nw] = 1
    
    return -1
        

sol = -1
H, W, R, C, S, K = Input_Data()
sol = BFS()
print(sol)