#1,2,3,4,5,6,... 에서 틀림 높은 수는 정답 맞음
N = int(input())
s=N**(1/2)
s2=N**(1/2)
while(True):
    print("s:",s)
    t=int(s)
    if t*(t+1)/2>N:
        if N == 1:
            print(1)
            break
        print(int(s-s2))
        break
    s2=s2**(1/2)
    s+=s2
