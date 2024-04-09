n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans =0
for i in range(n):
    for j in range(n):
        tmp =0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if in_range(nx,ny) and board[nx][ny] == 1:
                tmp+=1
        if tmp >=3:
            
            ans+=1

print(ans)