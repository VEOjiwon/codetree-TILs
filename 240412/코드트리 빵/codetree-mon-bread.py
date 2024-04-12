'''
1번 사람 1분, 2번사람 2분..에 출발, 사람들은 목표 편의점이 다 다름
nxn 격자 위에서 진행, m번 사람
1분동안 진행되는 행동 3
[1] 본인이 가고싶은 편의점 방향으로 1칸 (최단거리, 상좌우하 우선순위)
    최단거리: 거처야하는 칸의 수가 최소로 되는 거리
[2] 편의점 도착시, 해당 편의점에서 멈추고 다른사람들은 해당 칸에 통행 못함
    단, 격자에 있는 사람이 모두 이동 후에 갈 수 없음
[3] 현재 시간이 t분, t<=m 만족시, t 번 사람은 자신이 가고 싶은 편의점과 가장
    가까이 있는 베이스 캠프에 들어감 (최단거리, 행작, 열작)
    베이스 캠프 이동시엔 시간 소모x
    이 때 부터는 다른 사람들은 해당 칸 지날 수 없음, 격자에 있는 사람이 모두 이동 후에
    갈 수 없음
'''
import sys


n, m = map(int, sys.stdin.readline().split())
board = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
dest = list(list(map(int,sys.stdin.readline().split())) for _ in range(m))

for i in range(len(dest)):
    dest[i] = [dest[i][0]-1, dest[i][1]-1]
basecamp = []
people = []
in_board = [0] * m


# 편의점 초기 위치는 -2로, 도착 시 -1
# basecamp -> 초기엔 -3, 해당 idx 번호로
# 비어있는 칸 -> -4

for x,y in dest:
    board[x][y] = -2

# basecamp 좌표 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = -4
        if board[i][j] == 1:
            basecamp.append((i,j))
            board[i][j] = -3

# menhattan distance
def get_dist(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)

dxs=[-1,0,0,1]
dys=[0,-1,1,0]
def find_basecamp(cur):
    comp = []
    tx, ty = dest[cur]
    for idx, (cx,cy) in enumerate(basecamp):
        if board[cx][cy] == -3:
            comp.append([get_dist(tx,cx,ty,cy),cx,cy])
    comp.sort(key= lambda x: (x[0],x[1],x[2]))
    return comp[0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n


def moving_people():
    global board
    for i in range(m):
        if in_board[i] ==0:
            continue
        cx,cy = people[i]
        tx,ty = dest[i]
        temp = []
        for j in range(4):
            nx = cx + dxs[j]
            ny = cy + dys[j]
            if in_range(nx,ny) and (board[nx][ny] == -4 or board[nx][ny]==i or board[nx][ny] == -2 or board[nx][ny] == -3):
                temp.append([get_dist(nx, tx, ny, ty),j,nx,ny])

        temp.sort(key=lambda x: (x[0],x[1]))
        _,_, gx,gy = temp[0]

        if gx == tx and gy == ty:

            in_board[i] = 0
            board[tx][ty] = -1

        people[i] = [gx, gy]




turn = 0
# print('turn :', turn)
# print(people)
# print(dest)
# for elem in board:
#     print(*elem)
while True:
    # 편의점이 모두 통행 불가능한 경우 (사람이 가있는 경우)
    cnt = 0
    for x,y in dest:
        if board[x][y]==-1:
           cnt += 1
    if cnt == len(dest):
        print(turn)
        break

    # 베이스 캠프 입소식
    bx,by = -1,-1
    newbie = -1
    if turn < m:
        dist, bx, by = find_basecamp(turn)
        people.append([bx,by])
        newbie = turn

    moving_people()

    if bx != -1:
        # 사람들 이동후 통행 불가
        board[bx][by] = turn
    if newbie !=-1:
        in_board[turn] = 1

    if turn > 9:
        break

    turn +=1
    # print('turn :', turn)
    # print(people)
    # print(dest)
    # for elem in board:
    #     print(*elem)