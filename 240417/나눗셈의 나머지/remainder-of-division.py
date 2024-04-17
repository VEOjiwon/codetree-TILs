a, b = map(int, input().split())
tmp = [0] * (b)
while a>1:
    tmp[a % b] +=1
    a //= b

ans=0
for i in tmp:
    ans += i**2
print(ans)