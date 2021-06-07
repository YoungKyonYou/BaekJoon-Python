
N=int(input())
R=1000-N
a=R//500
b=R%500//100
c=R%100//50
d=R%50//10
e=R%10//5
f=R%5

print(a+b+c+d+e+f)