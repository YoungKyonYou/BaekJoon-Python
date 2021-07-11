def solution(number, k):
    stack = ['A', number[0]]
    a = k
    for i in range(1, len(number)):
        while k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    if k != 0:
        return ''.join(stack[1:-k])
    return ''.join(stack[1:])


n = "01010"
k = 3
11

solution(n, k)
