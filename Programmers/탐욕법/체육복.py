import sys
from typing import overload
input = sys.stdin.readline


def solution(n, lost, reserve):
    answer = 0
    answer1 = 0
    answer2 = 0
    lost.sort()
    reserve.sort()

    overlap = []
    pair = []

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                overlap.append(lost[i])

    print('overlap:', overlap)

    for i in range(len(overlap)):
        lost.remove(overlap[i])
        reserve.remove(overlap[i])

    for i in range(len(reserve)):
        pair.append([reserve[i], 0])

    print('lost:', lost)
    print('reserve:', reserve)
    print('pair:', pair)
    temp = lost+reserve

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if reserve[j] == lost[i]-1:
                pair[j][1] = 1
                answer1 += 2
                break

    print('pair1:', pair, 'answer1:', answer1)
    for i in range(len(pair)):
        if pair[i][1] == 0:
            answer1 += 1
        pair[i][1] = 0
    print('after pair1 answer1:', answer1)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if reserve[j] == lost[i]+1:
                pair[j][1] = 1
                answer2 += 2
                break

    print('pair2:', pair, 'answer2:', answer2)
    for i in range(len(pair)):
        if pair[i][1] == 0:
            answer2 += 1
        pair[i][1] = 0
    print('after pair2 answer2:', answer2)

    print(answer1)
    print(answer2)
    if answer1 < answer2:
        answer = answer2
    else:
        answer = answer1
    print('n-len(temp):', n-len(temp))
    print(answer+(n-len(temp)))


'''
n = 5
l = [2, 4]
r = [1, 3, 5]


n = 3
l = [3]
r = [1]

n=5
l=[2,4]
r=[3]
t=l+r

n = 5
l = [2, 3, 4]
r = [3, 4, 5]
t = l+r

n=4
l=[4,2]
r=[1,3]
4

'''
n = 5
l = [3, 4]
r = [4, 5]

solution(n, l, r)
