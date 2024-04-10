import sys
import heapq

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

q = []
ans = 0

for num in nums:
    heapq.heappush(q, num)

while len(pq) > 1:
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)

    ans += (x1+x2)
    heapq.hezppus(pq,x1+x2)

print(ans)