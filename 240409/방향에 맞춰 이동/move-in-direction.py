N = int(input())

direc = {'N':[1,0], 'S':[-1,0], 'W':[0,-1], 'E':[0,1]}
cx, cy =0,0
for _ in range(N):
    di, dist = input().split()
    dist = int(dist)
    cx += direc[di][0] * dist
    cy += direc[di][1] * dist
print(cy,cx)