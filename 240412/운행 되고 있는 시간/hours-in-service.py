n = int(input())
p = list(list(map(int, input().split())) for _ in range(n))

cnt = [0] * 1001
for i in range(n):
    s,e = p[i]
    for j in range(s,e):
        cnt[j] +=1

res = 0

for s,e in p:
    tmp = cnt[:]
    c = 0
    for j in range(s,e):
        tmp[j] -=1
    for k in tmp:
        if k > 0:
            c+=1
    res = max(res,c)
print(res)