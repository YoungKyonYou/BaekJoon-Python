import sys
input=sys.stdin.readline
n=int(input())
e=[]
for i in range(n):
    num=int(input())
    e.append(num)
e.sort(reverse=True)
max=-1
for i in range(len(e),0,-1):
    m=e[i-1]*i
    if m>max:
        max=m
print(max)