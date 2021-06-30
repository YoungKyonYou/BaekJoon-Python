from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


n = [1, 1, 1, 1, 1]
t = 3
solution(n, t)
