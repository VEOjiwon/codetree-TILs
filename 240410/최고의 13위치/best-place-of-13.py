import sys
n = int(input())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
ans = 0
for i in range(n):
    for j in range(n-2):
            ans = max(ans, board[i][j]+board[i][j+1]+board[i][j+2])
print(ans)