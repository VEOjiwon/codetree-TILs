n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for k in range(3):
            for l in range(3):
                tmp+=board[i+k][j+l]
        ans = max(ans,tmp)
print(ans)