import sys
n = int(input())
ckpts = list(list(map(int,input().split())) for _ in range(n))

min_dist = sys.maxsize

def get_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

for i in range(1,len(ckpts)-1):
    tmp = 0
    tmp_elem = ckpts.pop(i)
    for j in range(1,len(ckpts)):
        tmp+=get_dist(ckpts[j][0], ckpts[j][1],ckpts[j-1][0], ckpts[j-1][1])
    ckpts.insert(i,tmp_elem)
    min_dist = min(min_dist, tmp)
print(min_dist)