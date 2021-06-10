import sys
input = sys.stdin.readline

N = int(input())
l = []
for i in range(N):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    l.append((num2, num1))

l.sort()
ans = 1

temp = l[0][0]
for i in range(1, N):
    if(temp <= l[i][1]):
        
        ans += 1
        temp = l[i][0]

print(ans)
