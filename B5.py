import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	package = list(map(int,readl().split()))
	return N, package


sol = -1
# 입력받는 부분
N, package = Input_Data()

# 여기서부터 작성
sol = 0
while True:
    package.sort()
    try:
        p_cost = (package.pop(0) + package.pop(0))
    except:
        sol += p_cost
        break
    sol += p_cost
    if len(package) == 0:
        break
    package.append(p_cost)

# 출력하는 부분
print(sol)