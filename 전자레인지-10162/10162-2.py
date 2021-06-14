import sys
input=sys.stdin.readline
num = int(input())
a = num//300
b = num % 300//60
if num % 10 == 0:
    print(a, b, num % 300 % 60//10)
else:
    print(-1)
