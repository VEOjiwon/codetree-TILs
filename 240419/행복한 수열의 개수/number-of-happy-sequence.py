n,k = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
ans = 0
for i in range(n):
    max_conseq = 1
    for j in range(n-1):
        if board[i][j] == board[i][j+1]:
            max_conseq +=1
        else:
            max_conseq=1
    if max_conseq >=k:
        ans+=1

for i in range(n):
    max_conseq = 1
    for j in range(n-1):
        if board[j][i] == board[j+1][i]:
            max_conseq +=1
        else:
            max_conseq=1
    if max_conseq >=k:
        ans+=1
print(ans)