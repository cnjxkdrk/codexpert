import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    sw, sh, ew, eh = map(int, readl().split())
    map_maze = [list(map(int, readl().rstrip())) for _ in range(H)]
    return W, H, sw-1, sh-1, ew-1, eh-1, map_maze

def BFS():
    q = deque()
    q.append((sh, sw, 0))
    map_maze[sh][sw] = 1
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]

    while q:
        ch, cw, ctime = q.popleft()
        for i in range(4):
            nh = ch + dh[i]
            nw = cw + dw[i]
            ntime = ctime + 1
            if nh<0 or nh>=H or nw<0 or nw>=W: continue
            if map_maze[nh][nw] == 1: continue
            if nh==eh and nw==ew: return ntime
            q.append((nh, nw, ntime))
            map_maze[nh][nw] = 1

    return -1

W, H, sw, sh, ew, eh, map_maze = Input_Data()
sol = BFS()
print(sol)
