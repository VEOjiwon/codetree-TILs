import sys
n, m = map(int,sys.stdin.readline().split())
board = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))

ans = 0
if m == 1:
    print(2*n)
else:
    for i in range(n):
        tmp=0
        tmax = 0
        cmax = 0
        ctmp = 0
        for j in range(n):
            if i ==0:
                prev2 = board[j][i]
            elif prev2 == board[j][i]:
                ctmp +=1
                cmax = max(cmax,ctmp)
            else:
                ctmp = 0
            prev2 = board[j][i]
            
            if j==0:
                prev = board[i][j]
            elif prev == board[i][j]:
                tmp+=1
                tmax = max(tmax,tmp)
            else:
                tmp = 0
            prev = board[i][j]

        if tmax>=m-1:
            ans+=1
        if cmax>=m-1:
            ans+=1
    print(ans)