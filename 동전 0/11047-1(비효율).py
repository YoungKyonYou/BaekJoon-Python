N,K=input().split()
N=int(N)
K=int(K)
l=[]
ans=0
for i in range(N):
    l.append(int(input()))
cnt=len(l)
while(K):
    if K<l[cnt-1]:
        cnt-=1
    else:
        K-=l[cnt-1]
        ans+=1
print(ans)