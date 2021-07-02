
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    Q = [begin]
    while True:
        temp_Q=[]
        for w in Q:
            idx = 0
            if w==target:
                print(answer)
                return answer
            for _ in range(len(words)):
                tmp = words[idx]
                if sum(a != b for a, b in zip(w, tmp)) == 1:
                    temp_Q.append(words.pop(idx))
                    idx-=1
                idx += 1
        

        answer += 1
        Q=temp_Q
        if begin == temp_Q[0]:
            break


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
