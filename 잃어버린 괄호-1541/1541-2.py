e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e)
print(e[0]-sum(e[1:]))