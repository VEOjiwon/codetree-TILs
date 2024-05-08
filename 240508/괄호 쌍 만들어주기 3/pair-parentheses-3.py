from collections import deque

target = input().rstrip()
q = deque()
cnt = 0
n = len(target)
for i in range(n):
    if target[i] == '(':
        for j in range(i+1,n):
            if target[j] == ')':
                cnt+=1
print(cnt)