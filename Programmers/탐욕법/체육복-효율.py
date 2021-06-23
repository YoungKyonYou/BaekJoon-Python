def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        print('r:',r)
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    print('answer:',n-len(_lost))
    return n - len(_lost)


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
