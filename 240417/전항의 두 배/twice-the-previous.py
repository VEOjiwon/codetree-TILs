a,b = map(int, input().split())

arr = [a,b]
for i in range(1,11):
    arr.append(2*arr[i-1]+arr[i])
print(*arr[:10])