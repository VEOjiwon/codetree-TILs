n, m = map(int, input().split())
board1 = list(list(map(int, input().split())) for _ in range(n))
board2 = list(list(map(int, input().split())) for _ in range(n))

ans = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board1[i][j] == board2[i][j]:
            ans[i][j] = 0
        else:
            ans[i][j] = 1

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()