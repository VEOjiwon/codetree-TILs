import sys

n,k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(n-k):
    res = max(res, sum(arr[i:i+k+1]))
print(res)