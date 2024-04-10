import sys
n,m = map(int, sys.stdin.readline().split())
board = list(list(sys.stdin.readline().split()) for _ in range(n))

ans = 0

for i in range(1,n):
    for j in range(1,m):
        for k in range(i+1,n-1):
            for l in range(j+1,m-1):
                if board[0][0] != board[i][j] and board[i][j] != board[k][l] and \
                    board[k][l] != board[n-1][m-1]:
                    ans+=1
print(ans)