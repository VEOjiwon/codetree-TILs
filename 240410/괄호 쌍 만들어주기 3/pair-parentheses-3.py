import sys

A = sys.stdin.readline()
n = len(A)
ans = 0
for i in range(n-1):
    if A[i] == '(':
        for j in range(i,n):
            if A[j] ==')':
                ans+=1
print(ans)