import sys
n = int(input())
grid = list(map(int, input().split()))
ans = sys.maxsize
for i in range(n):
    tmp_ans = 0
    for j in range(i+1,n):
        tmp_ans += abs(j-i) * grid[j]
    for j in range(i-1,-1,-1):
        tmp_ans += abs(j-i) * grid[j]
    ans = min(ans, tmp_ans)
print(ans)