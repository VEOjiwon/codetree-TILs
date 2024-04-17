n = int(input())
arr = list(map(int, input().split()))

tmp = []
for i in arr:
    if i % 2 ==0:
        tmp.append(i)
tmp.reverse()

print(*tmp)