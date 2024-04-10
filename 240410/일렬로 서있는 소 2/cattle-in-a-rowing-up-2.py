import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if A[i] <= A[j] and A[j] <= A[k]:
                
                ans += 1

print(ans)