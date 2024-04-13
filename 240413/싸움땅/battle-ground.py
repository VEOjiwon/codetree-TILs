'''
nxn 크기 격자
무기 없는 빈 격자 시작, 플레이어 초기 능력치 있음
[1] 순차적으로 본인이 향하고 있는 방향대로 한칸, 격자 나갈 시 반대로 한칸
[2] 이동한 방향에 플레이어가 없으면 -> 총이 있는지 확인
    총이 있는 경우, 본인총 보다 센 경우만 총 획득
[3] 플레이어가 있으면 결투 -> 플레이어 능력치 + 총의 공격력 합
    같은경우 -> 플레이어 초기 능력치가 높은사람 승
    이긴 플레이어: 차이만큼 포인트로 획득, 한칸 떨어진 총들 중 공격력 높은것과 교환
    진 플레이어: 본인 총을 격자에 내려놓고 원래 가지고 있던 방향대로 한칸이동
    이동하려는 칸에 다른 플레이어 있거나 범위 밖은, 오른쪽 90도씩 회전
    빈 칸이 보이는 순간 이동, 해당 칸에 총이 있다면 총 획득
1~n번 플레이어 까지 순차적으로 1번씩 진행 하면 1라운드 종료
'''
import sys

n,m,k = map(int, sys.stdin.readline().split())

guns= list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
player = list(list(map(int, sys.stdin.readline().split())) for _ in range(m))
gun_li = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        gun_li[i][j] = [guns[i][j]]

for i in range(m):
    cx,cy,d,s = player[i]
    player[i] = cx-1,cy-1,d,s,0


# x, y, d, s에다가 추가적으로 gun 능력치
point = [0] *(m)

# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]
from collections import deque
def move_lose(idx,lx,ly,ld,ls,lg):
    gun_li[lx][ly].append(lg)
    lg = 0

    
    while True:
        nx = lx + dx[ld]
        ny = ly + dy[ld]
        for j in range(m):
            if idx == j: continue
            kx,ky,kd,ks,kg = player[j]
            if (kx == nx and kx == ny) or not in_range(nx,ny):
                ld = (ld + 1) % 3
                break
        else:
            lg = max(gun_li[nx][ny])
            gun_li[nx][ny].remove(lg)
            if gun_li[nx][ny] == []:
                gun_li[nx][ny] = [0]
            break
    player[idx] = nx,ny,ld,ls,lg


def move_win(idx,wx,wy,wd,ws,wg):
    max_power = -1
    max_cord_x = 0
    max_cord_y = 0
    for i in range(4):
        nx = wx + dx[i]
        ny = wy + dy[i]
        if in_range(nx,ny):
            max_power = max(max_power, max(gun_li[nx][ny]))
            max_cord_x=nx
            max_cord_y=ny
    if max_power > wg:
        wg = max_power
        gun_li[max_cord_x][max_cord_y].remove(max_power)
        if gun_li[max_cord_x][max_cord_y] == []:
            gun_li[max_cord_x][max_cord_y] = [0]
    player[idx] = wx,wy,wd,ws,wg

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def is_empty(li):
    if li == []:
        return True

for turn in range(1,k+1):
    
    for i in range(m):
        
        cx,cy,d,s,g = player[i]
        nx = cx + dx[d]
        ny = cy + dy [d]
        # 격자에서 나갈 경우
        if not in_range(nx,ny):
            nx = cx - dx[d]
            ny = cy - dy [d]
        for j in range(m):
            if i == j: # 자기 자신에 대해서는 생략
                continue
            
            tx,ty,td,ts,tg = player[j]
            

            # 다른 플레이어 만난 경우
            if nx == tx and ny == ty:
                # 뭔가 액션해야함
                moved_power = s+g
                meet_power = ts+tg
                
                if moved_power > meet_power:
                    point[i] += moved_power - meet_power
                    move_lose(j,tx,ty,td,ts,tg)
                    move_win(i,nx,ny,d,s,g)
                    

                elif moved_power < meet_power:
                    point[j] = meet_power - moved_power
                    move_lose(i,nx,ny,d,s,g)
                    move_win(j,tx,ty,td,ts,tg)
                    
                elif moved_power == meet_power:
                    if s > ts:
                        move_lose(j,tx,ty,td,ts,tg)
                        move_win(i,nx,ny,d,s,g)
                    else:
                        move_lose(i,nx,ny,d,s,g)
                        move_win(j,tx,ty,td,ts,tg)
                        
                break # break 지워선 안됌
        # 다른 플레이어를 만나지 않은 경우
        else:
            # 판에 총이 있는 경우
            if  len(gun_li[nx][ny]) >0 and gun_li[nx][ny][0] != 0:
                mpower = -1
                # 보드판의 총 중 가장 강력한 총 찾기
                
                mpower = max(mpower, max(gun_li[nx][ny]))
                # 플레이어가 총이 없는 경우
                if g == 0:
                    gun_li[nx][ny].remove(mpower)
                    if gun_li[nx][ny] == []:
                        gun_li[nx][ny] = [0]

                    
                    player[i] = nx,ny, d, s, mpower
                # 플레이어가 총이 있는 경우
                else:
                    if g < mpower:
                        gun_li[nx][ny].remove(mpower)
                        if gun_li[nx][ny] == []:
                            gun_li[nx][ny] = [0]
                        
                        gun_li[nx][ny].append(g)
                        player[i] = nx,ny,d,s, mpower
                    else:
                        player[i] = nx,ny,d,s,g
print(*point)