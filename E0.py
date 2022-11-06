import sys
import bisect

def Input_Data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    spot = list(map(int, readl().split()))
    tar = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, spot, tar

def Solve():
    sol = 0
    spot.sort()

    for x, y in tar:
        s = x - (L-y)
        e = x + (L-y)
        lower = bisect.bisect_left(spot, s)
        upper = bisect.bisect_right(spot, e)
        if (upper-lower) > 0:
            sol += 1

    return sol


M, N, L, spot ,tar = Input_Data()
sol = Solve()
print(sol)