str=input()
ans=0
idx=0
num1=""
num2=0
stack2=[]
op=""
num=[]
for i in range(len(str)):
    if str[idx]=='-' or str[idx]=='+':
        num.append(int(num1))
        num1=""
        num.append(str[idx])
        idx+=1
        continue
    num1+=str[idx]
    idx+=1
num.append(int(num1))
#print(num)
while(len(num)):
    n1=num.pop();
    if len(num)==0:
        stack2.append(n1)
        break
    op=num.pop();
    if op=='-':
        stack2.append(n1)
        stack2.append(op)
        continue
    n2=num.pop();
    num.append(n1+n2)
   # print(num)

while len(stack2):
    number1=stack2.pop()
    if len(stack2)==0:
        break
    operand=stack2.pop()
    number2=stack2.pop()
    stack2.append(number1-number2)

print(number1)
