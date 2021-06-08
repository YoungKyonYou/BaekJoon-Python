N, K = map(int, input().split())
l = []
ans = 0
for i in range(N):
    l.append(int(input()))
while(K):
    coin = l.pop()
    ans += K//coin
    K %= coin
print(ans)
