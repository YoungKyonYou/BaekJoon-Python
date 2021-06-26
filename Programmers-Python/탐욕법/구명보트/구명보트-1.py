def solution(people, limit):
    answer = 0
    people.sort()
    fidx,ridx=0,len(people)-1
    while fidx<ridx:
        if people[fidx]+people[ridx]>limit:
            answer+=1
            ridx-=1
        else:
            answer+=1
            fidx+=1
            ridx-=1
    return answer+1 if fidx==ridx else answer