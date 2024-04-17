a = input().rstrip()
b = input().rstrip()

tmp = a
for i in range(1,len(a)+1):
    tmp = tmp[-1] + tmp[:-1]
    if tmp == b:
        print(i)
        break
else:
    print(-1)