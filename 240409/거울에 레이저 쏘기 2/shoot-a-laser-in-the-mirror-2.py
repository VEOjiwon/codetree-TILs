N = int(input())
board = list(input().rstrip() for _ in range(N))
K = int(input())


mok = N // K # 1
left = N % K # 1
if mok == 0:
    prev_x = -1
    prev_y = left
    cx = 0
    cy = left 
elif mok ==1:
    prev_y = N
    prev_x = left 
    cy = N-1
    cx = left 
elif mok == 2:
    prev_x = N
    prev_y = left 
    cx = N-1
    cy = left 
elif mok == 3:
    prev_x = left
    prev_y = -1
    cx = left 
    cy = 0

def in_range(x,y):
    return 0<=x<N and 0<=y<N



ans = 0

while in_range(cx,cy):
    ans+=1
    cur = board[cx][cy]
    tmp_cx = cx
    tmp_cy = cy
    if cur == '/':
        # 상단
        if prev_x < cx and prev_y == cy:
            cy = cy -1
        # 좌단
        elif prev_x == cx and prev_y < cy:
            cx-=1
        # 우단
        elif prev_x == cx and prev_y >cy:
            cx+=1
        #하단
        else:
            cy+=1
    elif cur == '\\':
        # 상단
        if prev_x < cx and prev_y == cy:
            cy+=1
        # 좌단
        elif prev_x == cx and prev_y < cy:
            cx+=1
        # 우단
        elif prev_x == cx and prev_y >cy:
            cx-=1
        #하단
        else:
            cy-=1

    prev_x = tmp_cx
    prev_y = tmp_cy
print(ans)