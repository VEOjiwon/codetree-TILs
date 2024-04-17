n = int(input())

ans = [[1] * n for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        ans[i][j] = ans[i-1][j] + ans[i][j-1] + ans[i-1][j-1]

for elem in ans:
    print(*elem)