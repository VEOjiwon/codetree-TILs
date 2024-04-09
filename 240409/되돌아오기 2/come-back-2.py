cmds = input().strip()

dxs = [1,0,-1,0]
dys = [0,1,0,-1]

cur_dir = 0
cx, cy = 0,0
ans = 0
for cmd in cmds:
    ans+=1
    if cmd == "F":
        cx += dxs[cur_dir]
        cy += dys[cur_dir]
        if cx ==0 and cy == 0:
            print(ans)
            break

    elif cmd =='R':
        cur_dir = (cur_dir + 1) % 4
    elif cmd =='L':
        cur_dir = (cur_dir - 1 + 4) % 4
else:
    print(-1)