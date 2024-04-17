n = int(input())
ans = [[0] * n for _ in range(n)]
i, j = n-1,n-1
dxs = [-1,0,1,0]
dys = [0,-1,0,-1]
cur_d = 0
num = 1
for _ in range(n*n):
    ans[i][j] = num
    i += dxs[cur_d]
    j += dys[cur_d]
    num+=1
    if i == 0 or i == n-1:
        cur_d = (cur_d + 1) % 4

for elem in ans:
    print(*elem)