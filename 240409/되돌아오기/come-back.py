N = int(input())
cmds = list(tuple(input().split()) for _ in range(N))

dxs = [1,0,0,-1]
dys = [0,1,-1,0]
ddict = {'N':0,'E':1,'W':2,'S':3}
init_x, init_y = 0,0
cx, cy = init_x, init_y
ans = 0
flag=False
for turn, (cmd, dist) in enumerate(cmds):
    dist = int(dist)
    dx = dxs[ddict[cmd]]
    dy = dys[ddict[cmd]]
    for _ in range(dist):
        nx = cx + dx
        ny = cy + dy
        ans+=1
        if init_x == nx and init_y ==ny:
            print(ans)
            flag=True
            break
    
        cx = nx
        cy = ny
    if flag:
        break
    

else:
    print(-1)