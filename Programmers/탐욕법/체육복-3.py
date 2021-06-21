
import copy


def solution(n, lost, reserve):
    answer = 0
    answer1 = 0
    answer2 = 0

    flag1 = [0]*(n+1)
    flag2 = [0]*(n+1)
    fcnt1 = -1
    fcnt2 = -1
    h = 0
    temp = []

    lost.sort()
    reserve.sort()
    idx = 0
    h = lost+reserve
    answer += n-len(set(h))
    print('n-len of set(h):', n-len(set(h)))

    # 중복 제거및 answer 더해주기
    for _ in range(len(reserve)):
        if reserve[idx] in lost:
            lost.remove(reserve[idx])
            reserve.remove(reserve[idx])
            answer += 1
        else:
            idx += 1
    ltemp = copy.deepcopy(lost)

    idx1 = 0

    for _ in range(len(ltemp)):
        l = ltemp[idx1]+1
        if reserve.count(l) == 1:
            ltemp.remove(l)
            reserve.remove(l)
            idx1 -= 1
        idx1 += 1

    idx1 = 0

    for _ in range(len(ltemp)):
        l = ltemp[idx1]-1
        if reserve.count(l) == 1:
            ltemp.remove(l)
            reserve.remove(l)
            idx1 -= 1
        idx1 += 1

    print('lost:', ltemp)
    print('reserve:', reserve)
    print(n-len(ltemp))


n = 5
l = [1, 2, 3]
r = [3, 4, 5]
4
'''
n = 5
l = [2, 4]
r = [1, 3, 5]
5

n = 3
l = [3]
r = [1]
2

n=5
l=[2,4]
r=[3]
t=l+r
4

n = 5
l = [2, 3, 4]
r = [3, 4, 5]
t = l+r
4

n=4
l=[4,2]
r=[1,3]
4

n = 5
l = [3, 4]
r = [4, 5]
4

n = 5
l = [1,2,3,4,5]
r = [1,2,3,4,5]
5

n=10
l=[5,4,3,2,1]
r=[3,1,2,5,4]
10

n=10
l=[8,10]
r=[6,7,9]
10

n=5
l=[2,3,4]
r=[1,2,3]
4

n=4
l=[3,1]
r=[2,4]
4

n=4
l=[4,2]
r=[1,3]
4

n=10
l=[5,7,9]
r=[1,2,3,4,6,8]
10

n=5
l=[3,1]
r=[2,3]
5

n=2
l=[1]
r=[2]
2

n=5
l=[1]
r=[1]
5

n=7
l=[2,4,5,6,7]
r=[1,3,4,5,6,7]
7

n=7
l=[1,2,3,4,5,6,7]
r=[1,2,3]
7

n=2
l=[2]
r=[1]
2

n=7
l=[2,3,4,6]
r=[1,2,3]
5

n=8
l=[1,2,4,6]
r=[1,2,4,6]
8
'''


solution(n, l, r)
