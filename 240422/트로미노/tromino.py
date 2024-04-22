import sys
n,m = map(int,input().split())
board = list(list(map(int, input().split())) for _ in range(n))

ans = -1

for i in range(n):
    for j in range(m):

        if i < n-1 and j < m-1:
            # 첫 번쨰
            tmp = 0
            tmp_min=sys.maxsize
            for k in range(i,i+2):
                for l in range(j,j+2):
                    tmp+=board[k][l]
                    tmp_min = min(tmp_min, board[k][l])
            ans = max(ans, tmp - tmp_min)
        # 두 번째
        if j < m - 3:
            tmp = 0
            for k in range(j,j+4):
                tmp+= board[i][k]
            ans = max(ans, tmp - tmp_min)
        if i < n - 3:
            tmp = 0
            for k in range(i,i+4):
                tmp+= board[k][j]
            ans = max(ans, tmp - tmp_min)
print(ans)