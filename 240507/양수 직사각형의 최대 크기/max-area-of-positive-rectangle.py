n,m = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(n))

def is_pos(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if grid[i][j] < 0:
                return False
    return True

def search_square(grid,n,m):
    max_size = -1
    # 직사각형 꼭지점 좌표 4개
    for i in range(n):
        for j in range(m):
            for k in range(i+1,n):
                for l in range(j+1,m):
                    if is_pos(i,j,k,l):
                        size = (k-i+1) * (l-j+1)
                        max_size = max(max_size, size)
    return max_size

print(search_square(grid,n,m))