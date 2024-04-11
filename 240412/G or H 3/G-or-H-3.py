import sys

n, k = map(int, sys.stdin.readline().split())

p = [0] * 10001

for _ in range(n):
    idx, tp = sys.stdin.readline().split()
    if tp == 'G':
        p[int(idx)] += 1
    elif tp == 'H':
        p[int(idx)] += 2

ans = -1

for i in range(len(p)-k):
    ans = max(ans, sum(p[i:i+k+1]))
print(ans)