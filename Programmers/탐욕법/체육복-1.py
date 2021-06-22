
import copy


def solution(n, lost, reserve):
    answer = 0
    idx = 0
    a = [x for x in range(1, n+1)]
    for i in range(len(lost)):
        if lost[idx] in reserve:
            reserve.remove(lost[idx])
            a.remove(lost[idx])
            lost.remove(lost[idx])
            answer += 1
            idx -= 1
        idx += 1
    idx = 0
    for i in range(len(lost)):
        if lost[idx]+1 in reserve:
            reserve.remove(lost[idx]+1)
            a.remove(lost[idx]+1)
            a.remove(lost[idx])
            lost.remove(lost[idx])
            idx -= 1
            answer += 2
        idx += 1
    print('after one plus')
    print('lost:', lost)
    print('reserve:', reserve)
    print('answer:', answer, end="\n\n")
    idx = 0
    for i in range(len(lost)):
        if lost[idx]-1 in reserve:
            reserve.remove(lost[idx]-1)
            a.remove(lost[idx])
            a.remove(lost[idx]-1)
            lost.remove(lost[idx])
            idx -= 1
            answer += 2
        idx += 1
    a = list(set(a)-set(lost))
    a = list(set(a+reserve))
    print('after one minus')
    print('lost:', lost)
    print('reserve:', reserve)
    print('a:', a)
    print('answer plus reserve:', answer+len(a))


n = 5
l = [2, 3, 4]
r = [3, 4, 5]
t = l+r
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
