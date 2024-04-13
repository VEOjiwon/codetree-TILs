n = int(input())
arr = list(map(int, input().split()))

new_arr = []
for i in range(n):
    new_arr.append([i,arr[i]])
new_arr.sort(key=lambda x: x[0])

fidx, first_min = new_arr[0]

flag=False
for i in range(1,n):
    if first_min == new_arr[i][1]:
        continue
    else:
        if i<n-1:
            for j in range(n):
                if new_arr[i][1] == new_arr[j][1]:
                    flag=True
                    break
        if not flag:
            print(new_arr[i][0]+1)
            break
else:
    print(-1)