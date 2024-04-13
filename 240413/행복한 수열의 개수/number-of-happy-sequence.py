n,m = map(int, input().split())
arr = list(list(map(int,input().split())) for _ in range(n))
ans = 0
seq = [0 for _ in range(n)]

def is_happy():
    conseq_cnt, max_ccnt = 1, 1
    for i in range(1,n):
        if seq[i-1] == seq[i]:
            conseq_cnt+=1
        else:
            conseq_cnt = 1
        max_ccnt = max(max_ccnt, conseq_cnt)
    return max_ccnt>=m

for i in range(n):
    seq = arr[i][:]

    if is_happy():
        ans+=1

for j in range(n):
    for i in range(n):
        seq[i] = arr[i][j]

    if is_happy():
        ans+=1
print(ans)