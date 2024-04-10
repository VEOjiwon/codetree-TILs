import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

min_val = sys.maxsize

for i in range(len(A)):
    tmp = 0
    for j in range(len(A)):
        if i == j:
            continue
        tmp+= abs(i-j) * A[j]
    
    if tmp < min_val:
        min_val = tmp
print(min_val)