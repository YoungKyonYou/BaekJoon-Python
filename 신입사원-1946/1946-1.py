import sys
input = sys.stdin.readline
l = []
N = int(input())
cnt = 1
minF = 0
minS = 0
for i in range(N):
    T = int(input())
    for j in range(T):
        a, b = map(int, input().split())
        l.append((a, b))
    l.sort()
    minF = l[0][0]
    minS = l[0][1]
    for k in range(len(l)-1):
        a = l[k+1][0]
        b = l[k+1][1]
        if a < minF:
            minF = a
            cnt += 1
        if b < minS:
            minS = b
            cnt += 1
    print(cnt)
    cnt = 1
    l = []
