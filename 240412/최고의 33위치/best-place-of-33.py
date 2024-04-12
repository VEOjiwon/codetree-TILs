n = int(input())
board=list(list(map(int, input().split()))for _ in range(n))
res = 0
for i in range(n-2):
    for j in range(n-2):
        res = max(res,sum(map(sum,board[i:i+3][j:j+3])))
print(res)