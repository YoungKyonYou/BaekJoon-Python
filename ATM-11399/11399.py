a = int(input())
l = []
total = 0
cur = 0
l = list(map(int, input().split()))

l.sort()
for x in l:
    cur += x
    total += cur
print(total)