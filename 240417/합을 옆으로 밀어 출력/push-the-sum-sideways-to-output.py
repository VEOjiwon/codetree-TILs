n = int(input())
arr = list(int(input().rstrip()) for _ in range(n))
ans = 0
for i in arr:
    ans += i

ans = list(str(ans))
ans.append(ans[0])
ans.pop(0)
print(''.join(ans))