n,k = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
ans = 0

if n == 1 and k == 1:
    print(2)
else:

    for i in range(n):
        max_conseq = 1
        local_max = 0
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                max_conseq +=1
                
            else:
                max_conseq=1
            local_max = max(local_max, max_conseq)
        if local_max >=k:
            ans+=1

    for i in range(n):
        max_conseq = 1
        local_max = 0
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                max_conseq +=1
            else:
                max_conseq=1
            local_max = max(local_max, max_conseq)
        if local_max >=k:
            ans+=1
    print(ans)