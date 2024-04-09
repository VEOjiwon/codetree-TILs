n, t = map(int,input().split())
r,c,d = input().split()


dd = [[-1,0], [1,0], [0,1],[0,-1]]
ddict={'U':0,"D":1,"R":2,"L":3}
r = int(r)
c = int(c)


def in_range(x,y):
    return 0<x<=n and 0<y<=n
for _ in range(t):
    cur_d = ddict[d]
    nr = r + dd[cur_d][0]
    nc = c + dd[cur_d][1]
    if in_range(nr,nc):
        r = nr
        c = nc
    else:
        if d == 'L':
            d = 'R'
        elif d == 'R':
            d = 'L'
        elif d == 'U':
            d = 'D'
        else:
            d = 'U'
print(r,c)