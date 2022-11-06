# A5
# A9
# B5 SimpleSort
# C0
# C1
# C6
# C7
# C9 순열/조합


import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = list(map(int, readl().split()))
    return N, num
 
 
def Simple_Sort(s, e):
    for i in range(s, e):
        for j in range(i+1, e+1):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
 
N, num = Input_Data()
Simple_Sort(0, N-1)