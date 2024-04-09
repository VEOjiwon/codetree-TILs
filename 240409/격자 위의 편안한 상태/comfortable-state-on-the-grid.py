N, M = map(int,input().split())
board = [[0] * N for _ in range(N)]
cmds = [list(map(int,input().split())) for _ in range(M)]
dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

for x,y in cmds:
    x-=1
    y-=1
    board[x][y] = 1
    tmp = 0
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if in_range(nx,ny) and board[nx][ny] ==1:
            tmp +=1
    if tmp == 3:
        print(1)
    else:
        print(0)