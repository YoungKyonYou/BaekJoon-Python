import sys
sys.setrecursionlimit(10**6)

def dfs(V):
    visit[V]=1
    result1.append(V)
    for i in adj[V]:
        if visit[i]==0:
            visit[i]=1
            dfs(i)
    
def bfs(V):
    visit=[0]*(N+1)
    visit[V]=1
    result2.append(V)
    tmp=[V]
    while tmp:
        a=tmp.pop(0)
        for i in adj[a]:
            if visit[i]==0:
                visit[i]=1
                result2.append(i)
                tmp.append(i)
    



input = sys.stdin.readline
N, M, V = map(int, input().split())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(len(adj)):
    adj[i].sort()
visit=[0]*(N+1)
result1=[]
result2=[]
dfs(V)
bfs(V)

#언팩킹 기법
print(*result1)
print(*result2)