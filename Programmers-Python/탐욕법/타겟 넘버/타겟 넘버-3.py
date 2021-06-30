def dfs(numbers, sum,target, idx):
    if len(numbers)==idx:
        if target==sum:
            return 1
        return 0
    return dfs(numbers,sum+numbers[idx],target,idx+1)+dfs(numbers,sum-numbers[idx],target,idx+1)

def solution(numbers, target):
    answer=dfs(numbers,0,target,0)
    print('answer:',answer)
    return answer

answer=0
solution([1, 1, 1, 1, 1],3)