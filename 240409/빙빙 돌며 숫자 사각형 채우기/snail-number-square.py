n,m = map(int, input().split())

board = [[0]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
board[0][0] = 1
cx, cy = 0,0
cdir = 0
def in_range(x,y):
    return 0<=x<n and 0<=y<m
for i in range(2,n*m+1):
    nx = cx + dx[cdir]
    ny = cy + dy[cdir]

    if in_range(nx,ny) and board[nx][ny] ==0:
        board[nx][ny] = i
    else:
        cdir = (cdir + 1) % 4
        nx = cx + dx[cdir]
        ny = cy + dy[cdir]
        board[nx][ny] = i
    
    cx = nx
    cy = ny

for elem in board:
    print(*elem)