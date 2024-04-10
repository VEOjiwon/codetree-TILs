import sys
n, k = map(int,sys.stdin.readline().split())
money = list(int(sys.stdin.readline()) for _ in range(n))

money.sort(reverse=True)

tmp = k
ans = 0
for val in money:
    if tmp == 0:
        print(ans)
        break
    if tmp // val >= 0:
        ans += (tmp//val)
        tmp = tmp % val