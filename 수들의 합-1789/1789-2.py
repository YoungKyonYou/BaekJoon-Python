
N = int(input())
s = int(N**(1/2))+int(int(N**(1/2))**(1/2))
while(True):
    if N*2 < s**2+s:
        if N == 1:
            print(1)
            break
        print(s-1)
        break
    s += 1
