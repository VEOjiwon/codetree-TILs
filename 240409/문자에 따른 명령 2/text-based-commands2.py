cmd = input()

#  북 동 남 서
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cur_d = 0
cx, cy = 0, 0
for c in cmd:
    if c == 'L':
        cur_d = (cur_d -1 + 4) % 4
    elif c == 'R':
        cur_d = (cur_d + 1) % 4
    else:
        cx += dx[cur_d]
        cy += dy[cur_d]
print(cx,cy)