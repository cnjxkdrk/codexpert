import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	str_exp = readl().split()
	nums = list(map(int,str_exp[0::2]))
	op = str_exp[1::2]
	return N, nums, op


sol = -1
# 입력받는 부분
N, nums, op = Input_Data()

# 여기서부터 작성
stack = deque([nums[0]])
for i in range(N-1):
    if op[i] == '+':
        stack.append(nums[i+1])
    elif op[i] == '-':
        stack.append(-nums[i+1])
    elif op[i] == '*':
        stack.append(stack.pop()*nums[i+1])
    else:
        stack.append(int(stack.pop()/nums[i+1]))

sol = sum(stack)

# 출력하는 부분
print(sol)