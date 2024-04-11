import sys

n = int(sys.stdin.readline())

cord = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
res = sys.maxsize
for i in range(n):
    max_x = 0
    min_x = 40001
    max_y = 0
    min_y = 40001
    for j in range(n):
        if i == j:
            continue
        x, y = cord[j]
        max_x = max(x,max_x)
        min_x = min(x,min_x)
        max_y = max(y,max_y)
        min_y = min(y, min_y)
    
    res = min((max_x - min_x) * (max_y-min_y), res)
print(res)