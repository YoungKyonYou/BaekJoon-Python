import sys
input = sys.stdin.readline
N = int(input())
s = int(N**(1/2))
s2 = 0
while(True):
    s2 = s**2+s
    if N*2 < s2:
        if N == 1:
            print(1)
            break
        print(s-1)
        break
    s += 1
