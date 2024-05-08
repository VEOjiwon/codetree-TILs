n,m = map(int, input().split())
board = list(list(input().split()) for _ in range(n))

cnt = 0
for i in range(1,n):
    for j in range(1, m):
        for k in range(i+1, n-1):
            for l in range(j+1,m-1):
                if board[0][0] != board[i][j] and board[i][j] != board[k][l] and board[k][l] != board[n-1][m-1]:
                    cnt+=1

print(cnt)