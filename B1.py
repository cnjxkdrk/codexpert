import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = list(map(int, readl().split()))
	return N, num

def SimpleSort(s, e):
    for i in range(s, e):
        for j in range(i+1, e+1):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]

# 입력받는 부분
N, num = Input_Data()

# 여기서부터 작성
SimpleSort(0, N-1)

# 출력하는 부분
print(*num)