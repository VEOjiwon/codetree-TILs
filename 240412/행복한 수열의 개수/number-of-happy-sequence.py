import sys
n, m = map(int,sys.stdin.readline().split())
board = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))

ans = 0

for i in range(n):
    tmp=1
    tmax = 0
    cmax = 0
    ctmp = 1
    for j in range(n):
        if i ==0:
            prev2 = board[j][i]
        elif prev2 == board[j][i]:
            ctmp +=1
            cmax = max(cmax,ctmp)
        else:
            ctmp = 1
        prev2 = board[j][i]
        if j==0:
            prev = board[i][j]
        elif prev == board[i][j]:
            tmp+=1
            tmax = max(tmax,tmp)
        else:
            tmp = 1
        prev = board[i][j]

    if tmax>=m:
        ans+=1
    if cmax>=m:
        ans+=1
print(ans)