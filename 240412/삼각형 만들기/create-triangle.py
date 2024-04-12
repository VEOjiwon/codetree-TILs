import sys

n = int(sys.stdin.readline())
cords = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))

def area(x1,x2,x3,y1,y2,y3):
    return abs((x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3))
res = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1, y1 = cords[i]
            x2, y2 = cords[j]
            x3, y3 = cords[k]
            if (y1 == y2 and x2 == x3) or (y1 == y2 and x1 == x3) or (y2 == y3 and x2 == x1) or (y2 == y3 and x3 == x1) or (y1 == y3 and x1 == x2) or (y1 == y3 and x1 == x3):
                res = max(res,area(x1,x2,x3,y1,y2,y3))
print(res)