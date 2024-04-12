n = int(input())
board=list(list(map(int, input().split()))for _ in range(n))
res = 0
for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for k in range(i,i+3):
            for l in range(j,j+3):
                tmp+= board[k][l]
        res = max(res,tmp)

print(res)