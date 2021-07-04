def dfs(tickets, v, n, flag, answer):
    flag[v] = 1
    answer.append(tickets[v])
    if len(answer) == n:
        return answer
    for i in range(len(tickets)):
        if tickets[v][1] == tickets[i][0] and flag[i] == 0:
            dfs(tickets, i, n, flag, answer)
            if len(answer) != n:
                flag[i] = 0
                answer.pop()
    return answer


def solution(tickets):
    answer = []
    n = len(tickets)
    tickets.sort()

    vList = []
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            vList.append(i)
    flag = [0]*n
    for i in range(len(vList)):
        answer = []
        flag = [0]*n
        flag[vList[i]] = 1
        answer = dfs(tickets, vList[i], n, flag, answer)
        if answer and len(answer) == n:
            ans = answer[0]
            t = sum(answer[1:], [])
            ans += t[1::2]
            return ans


#tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
#답:	["ICN", "B", "ICN", "A", "D", "A"]

tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], [
    "BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
#답:["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
#["ICN", "BOO"],["BOO", "DOO"],["DOO", "BOO"],["BOO", "ICN"],["ICN", "COO"],["COO", "DOO"],["DOO", "COO"],["COO", "BOO"],
solution(tickets)
