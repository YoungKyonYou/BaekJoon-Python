import sys
input = sys.stdin.readline

N = int(input())
l = [(*map(int, input().split()),) for _ in range(N)]
l.sort(key=lambda x: (x[1],x[0]))

ans = 1

temp = l[0][1]
for i in range(1, N):
    if(temp <= l[i][0]):
        ans += 1
        temp = l[i][1]

print(ans)
