import sys
import heapq
input = sys.stdin.readline
heap = []
ans=0
n = int(input())
for _ in range(n):
    heapq.heappush(heap, int(input()))
while len(heap) != 1:
    temp=heapq.heappop(heap)+heapq.heappop(heap)
    ans+=temp
    heapq.heappush(heap, temp)

print(ans)
