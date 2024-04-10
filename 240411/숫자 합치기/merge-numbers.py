import sys
import heapq

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

q = []
ans = 0

for num in nums:
    heapq.heappush(q, num)

while len(q) > 1:
    x1 = heapq.heappop(q)
    x2 = heapq.heappop(q)

    ans += (x1+x2)
    heapq.heappush(q,x1+x2)

print(ans)