n,m = map(int,input().split())
board = list(list(map(int,input().split())) for _ in range(n))

block1 = [[0,0],[1,0],[1,1]]
block2 = [[0,0],[0,1],[0,2]]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

# block 1
max_num = -1
for i in range(n-1):
    for j in range(m-1):
        partial = [row[j:j+2] for row in board[i:i+2]]
        partial_sum = sum(sum(row) for row in partial)
        partial_min = min(min(row) for row in partial)
        max_num =max(max_num, partial_sum - partial_min)

for i in range(n):
    for j in range(m-2):
        
        max_num = max(max_num, sum(board[i][j:j+3]))

for i in range(n-2):
    for j in range(m):
        
        max_num = max(max_num, board[i][j]+board[i+1][j]+board[i+2][j])
    
print(max_num)