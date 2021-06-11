e=input().split('-')
print(e)
sum=0
l=[]
for i in e[0].split('+'):
    sum+=int(i)
for i in e[1:]:
    for j in i.split('+'):
        sum-=int(j)
print(sum)
