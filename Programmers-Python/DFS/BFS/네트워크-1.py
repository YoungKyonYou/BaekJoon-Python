def dfs(n,computers,v, flag):
    for i in range(n):
        if flag[i]==0 and computers[v][i]==1:
            flag[i]=1
            dfs(n,computers,i,flag)
def solution(n, computers):
    answer = 0
    flag=[0]*n
    for i in range(n):
        if flag[i]==0:
            flag[i]=1
            dfs(n,computers,i,flag)
            answer+=1
    return answer

computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n=3
solution(n,computers)