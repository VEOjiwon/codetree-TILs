n = int(input())
board = list(list(map(int,input().split())) for _ in range(n))
ans = 0
for i in range(n):
    for j in range(n-2):
        tmp = 0 
        for k in range(j,j+3):
            tmp+= board[i][k]
        ans = max(ans,tmp)
print(ans)