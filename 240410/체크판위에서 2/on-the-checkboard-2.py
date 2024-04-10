import sys
n,m = map(int, sys.stdin.readline().split())
board = list(list(sys.stdin.readline().split()) for _ in range(n))

ws = []
bs = []
cur_c = board[0][0]
ans = 0
for i in range(n-1):
    for j in range(m-1):
        for k in range(i+1,n-2):
            for l in range(j+1,m-2):
                if board[k][l] != board[i][j]:
                    ans+=1
    
print(ans)