
def solution(name):
    answer = 0
    l = len(name)
    ptr = 0

    while True:
        # 현재 자리 알파벳으로 바꾸는데 드는 비용
        c = name[ptr]
        if ord(c)-65 <= 13:
            answer += ord(c)-65
        else:
            answer += 26+(65-ord(c))
        name = name[:ptr]+'A'+name[ptr+1:]
        # 왼쪽으로 갈지 오른쪽으로 갈지 결정
        lcnt, rcnt = 1, 1
        if name.count("A")==len(name):
            break

        # 왼쪽 먼저 살펴본다
        for i in range(ptr-1, ptr-len(name)+1, -1):
            if name[i] == 'A':
                lcnt += 1
            else:
                break
        for i in range(ptr+1, ptr+len(name)+1):
            if name[i % len(name)] == 'A':
                rcnt += 1
            else:
                break
        print('lcnt:', lcnt)
        print('rcnt:', rcnt)
        if lcnt < rcnt:
            answer += lcnt
            if ptr-lcnt < 0:
                ptr += len(name)
            ptr -= (lcnt)
            print('ptr:', len(name)-lcnt)
            print('len:', len(name))
        else:
            answer += rcnt
            ptr = (ptr+rcnt) % len(name)
            #ptr = (ptr+(rcnt)-len(name))

    print('answer:', answer)

    return answer


n = "ZZAAAZZ" 
8
solution(n)

'''
n="JEROEN"
56


n='JAN'
23

n='AAAA'
3

n='AAAAACAAAAAAAAABAA'
'''
