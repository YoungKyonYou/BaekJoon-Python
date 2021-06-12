import sys
input = sys.stdin.readline
N = int(input())
l=[0]*26
ans, num=0,9
for _ in range(N):
    s=input()
    for i in range(len(s)-1):
        l[ord(s[i])-ord('A')]+=10**(len(s)-i-2)

l.sort(reverse=True)
for i in l:
    ans, num=ans+i*num,num-1
print(ans)