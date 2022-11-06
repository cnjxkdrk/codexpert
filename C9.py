import sys

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	return N, M

def Solve():
    if M == 1: Dice1(0)
    elif M == 2: Dice2(0, 1)
    elif M == 3: Dice3(0)
    elif M == 4: Dice4(0, 1)

# 중복순열
def Dice1(n):
    if n >= N:
        print(*dice)
        return

    for i in range(1, 6+1):
        dice[n] = i
        Dice1(n+1)

# 중복조합
def Dice2(n, s):
    if n>=N:
        print(*dice)
        return

    for i in range(s, 6+1):
        dice[n] = i
        Dice2(n+1, i)

# 순열
def Dice3(n):
    if n >= N:
        print(*dice)
        return

    for i in range(1, 6+1):
        if sel[i]:
            continue
        dice[n] = i
        sel[i] = True
        Dice3(n+1)
        sel[i] = False

# 조합
# def Dice4(n, s):
#     if n>=N:
#         print(*dice)
#         return

#     for i in range(s, 6+1):
#         dice[n] = i
#         Dice4(n+1, i+1)
def Dice4(n, s):
    if n >= N:
        print(*dice)
        return

    for i in range(s, 6+1):
        if sel[i]:
            continue
        dice[n] = i
        sel[i] = True
        Dice4(n+1, i)
        sel[i] = False

# 입력 받는 부분
N, M = Input_Data()

# 여기서부터 작성
dice = [0]*N
sel = [False]*(6+1)

Solve()