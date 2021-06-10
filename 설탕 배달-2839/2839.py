num=int(input())
bags=0
while(num):
    if(num-3<0):
        bags=-1
        break
    if num%5==0:
        bags=int(num/5+bags)
        break
    else:
        num-=3
        bags+=1
print(bags)


