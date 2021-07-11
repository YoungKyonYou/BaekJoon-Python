def solution(number, k):
    answer = number
    while k != 0:
        c=int(answer[0])
        for i in answer[1:]:
            if c<int(i):
                idx=answer.find(str(c))
                answer=answer[:idx]+answer[idx+1:]
                k-=1
                break
            else:
                
                c=int(i)
    
    return answer


n = "4177252841"

solution(n, 4)
