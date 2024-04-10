import sys

n = int(sys.stdin.readline())
vec = list(map(int, sys.stdin.readline().split()))
ans = -1248000
i = 0
while i <n:
    
    range_sum = 0
    local_max = -127000
    
    for k in range(i,n):
        range_sum += vec[k]
        if local_max < range_sum:
            local_max = range_sum
        elif range_sum < 0:
            i+=k-1
            break

    ans = max(ans, local_max)
    i+=1

print(ans)