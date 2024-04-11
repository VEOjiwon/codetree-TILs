import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(n):
    for j in range(i,n):
        avg = sum(arr[i:j+1]) / (j-i+1)
        if avg in arr[i:j+1]:
            res+=1
print(res)