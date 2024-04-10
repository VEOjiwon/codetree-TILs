import sys

n = int(sys.stdin.readline())
time = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
time.sort(key= lambda x: x[1])
cur = time[0][1]
ans = 1
time = time[1:]

for s, e in time:
    if s >=cur:
        cur = e
        ans += 1

print(ans)