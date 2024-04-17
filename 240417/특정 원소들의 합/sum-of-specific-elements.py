board = list(list(map(int, input().split())) for _ in range(4))
ans = 0
for i in range(1,5):
    for j in range(i):
        ans += board[i-1][j]
print(ans)