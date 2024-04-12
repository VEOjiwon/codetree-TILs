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

# 이동 못하는 경우 -1
# 편의점 초기 위치는 2로
# basecamp 1
for x,y in dest:
    board[x][y] = 2

# basecamp 좌표 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            basecamp.append((i,j))

# menhattan distance
def get_dist(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)

dxs=[-1,0,0,1]
dys=[0,-1,1,0]
def find_basecamp(cur):
    comp = []
    tx, ty = dest[cur]
    for idx, (cx,cy) in enumerate(basecamp):
        if board[cx][cy] != -1:
            comp.append([get_dist(tx,cx,ty,cy),cx,cy])
    comp.sort(key= lambda x: (x[0],x[1],x[2]))
    return comp[0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n


def moving_people():
    arrive_this = []
    for i in range(m):
        if in_board[i] ==0:
            continue
        cx,cy = people[i]
        tx,ty = dest[i]
        cur_dist = get_dist(cx,tx,cy,ty)
        for j in range(4):
            nx = cx + dxs[j]
            ny = cy + dys[j]
            if in_range(nx,ny) and board[nx][ny] !=-1 and cur_dist > get_dist(nx,tx,ny,ty):
                # 편의점 도착 시
                if nx == tx and ny == ty:
                    in_board[i] = 0
                    arrive_this.append((tx,ty))

                people[i] = [nx, ny]
                break

    # 편의점 도착 경우 사람들 다 이동후 방출
    for x,y in arrive_this:
        board[x][y] = -1


turn = 0
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
        board[bx][by] = -1

    if newbie !=-1:
        in_board[turn] = 1
    turn +=1