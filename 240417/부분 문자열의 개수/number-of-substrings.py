str1 = input().rstrip()
target = input().rstrip()

cnt = 0
for i in range(len(str1)-1):
    if str1[i] + str1[i+1] == target:
        cnt+=1
print(cnt)