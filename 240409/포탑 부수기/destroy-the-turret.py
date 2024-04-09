'''
(1,1) 인덱스 시작
모든 위치 포탑존재, 공격력 0도 가능
K턴 반복, 부서지지 않은 포탑 1개가 있으면 즉시 중지
[1] 공격자 선정
부서지지 않은 포탑 중 가장 약한포탑 -> N + M 공격력 증가
    -> 1) 공격력 가장 낮음 2) 가장 최근 공격 3) 행열 합이 큼 4) 열값이 큼
[2] 공격자의 공격
자신 제외 가장 강한 포탑 공격
    -> 1) 공격력 가장 높음 2) 공격한지 가장 오래됨 3) 행열 합 작음 5) 열값이 작음
[3] 레이저 공격시도
    1) 우하좌상 4방향 2) 부서진 곳 (0) 있는곳 못지남
    3) 만약 끝지점 가면 반대로 이동
    4) 최단경로 이동 (BFS)
    5) 공격자의 공격력 만큼 피해 입힘, 레이저 경로에 있는 포탑도 공격력 // 2 만큼 공격받음
[4] [3] 실패시 포탄 공격
    1) 공격력 만큼 피해 2) 주위 8칸의 포탑은 공격력//2 만큼 피해
    3) 가장 자리면 반대편 까지 피해
[5] 포탑 정비
    1) 공격과 무관 했던 포탑 공격력 + 1 (공격자 x, 피해 x)
턴 종료 후 남아 있는 포탑 중 가장 강한 포탑 공격력
'''

import sys
from collections import deque


def find_defender(atx,aty):

    max_p = 0
    temp = []
    for i in range(N):
        for j in range(M):
            if 0 < board[i][j] and board[i][j] >= max_p:
                if i == atx and j==aty:
                    continue
                max_p = board[i][j]
                temp.append([board[i][j], attack_turn[i][j], i, j])
    # print(temp)
    temp.sort(key=lambda x: (x[0], -x[1], -(x[2] + x[3]), -x[3]), reverse=True)
    # for elem in board:
    #     print(*elem)
    return temp[0]

def find_attacker():
    min_p = sys.maxsize
    temp = []
    for i in range(N):
        for j in range(M):
            if 0 < board[i][j] <= min_p:
                min_p = board[i][j]
                temp.append([board[i][j], attack_turn[i][j], i, j])

    temp.sort(key=lambda x: (x[0], -x[1], -(x[2] + x[3]), -x[3]))
    return temp[0]
# 우하좌상
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def laser():
    dist =[[0]* N for _ in range(M)]
    q = deque()
    q.append((atx,aty))
    dist[atx][aty] = 1
    while q:
        x, y = q.popleft()
        if x == dfx and y == dfy:
            break
        for d in range(4):
            nx = (x + dxs[d]) % N
            ny = (y + dys[d]) % M
            if board[nx][ny] > 0 and dist[nx][ny]==0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    else:
        # 찾기 실패의 경우
        return False
    path = []
    q.clear()
    q.append((dfx, dfy))
    while q:
        x, y = q.popleft()
        if x == atx and y == aty:
            break
        for d in range(3,-1,-1):
            nx = (x + dxs[d]) % N
            ny = (y + dys[d]) % M
            if dist[nx][ny] == dist[x][y]-1:
                path.append((nx,ny))
                q.append((nx, ny))
                break

    path.pop()  # 공격한 곳 위치는 제거

    board[dfx][dfy] = max(board[dfx][dfy]-atpower,0)


    splash = atpower // 2
    # board에서 점수 제거
    for x,y in path:
        attacked[x][y] = 1
        board[x][y] = max(board[x][y] - splash, 0)

    return True

ddxs = [0,1,0,-1,-1,-1,1,1]
ddys = [1,0,-1,0,-1,1,-1,1]
def shot():
    # 8분위 탐색
    # dfx dfy
    sp_damaged = []
    for d in range(8):
        nx = (dfx + ddxs[d]) % N
        ny = (dfy + ddys[d]) % M
        if board[nx][ny] !=0:
            sp_damaged.append((nx,ny))
    splash = atpower // 2
    board[dfx][dfy] = max(board[dfx][dfy] - atpower, 0)
    for x,y in sp_damaged:
        attacked[x][y] = 1
        board[x][y] = max(0,board[x][y]-splash)
    return
def attack():
    if not laser():
        shot()

N, M, K = map(int, sys.stdin.readline().split())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
attack_turn = [[0] * M for _ in range(N)]

for turn in range(1,K+1):
    attacked = [[0] * M for _ in range(N)]
    # 공격 포탑 찾기
    _, _, atx, aty = find_attacker()
    board[atx][aty] += N+M
    atpower = board[atx][aty]
    attack_turn[atx][aty] = turn
    attacked[atx][aty] = 1

    # 방어 포탑 찾기
    dpower, _, dfx, dfy = find_defender(atx,aty)
    attacked[dfx][dfy] = 1

    # 공격 메커니즘
    attack()

    # 포탑 정비
    for i in range(N):
        for j in range(M):
            # 부서지지 않고 공격받지 않은 경우
            if board[i][j] > 0 and attacked[i][j] == 0:
                board[i][j]+=1

    # cnt = 0
    # for i in range(N):
    #     for j in range(M):
    #         if board[i][j] != 0:
    #             cnt+=1
    # if cnt < 2:
    #     print(1)
    #     break
    # for elem in board:
    #     print(*elem)
else:
    max_power = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > max_power:
                max_power = board[i][j]
    print(max_power)