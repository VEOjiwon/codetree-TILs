import sys

n = int(sys.stdin.readline())
vec = list(map(int, sys.stdin.readline().split()))
ans = -1248000
i = 0
while i <n:
    
    range_sum = vec[i]
    local_max = -127000
    
    for k in range(i+1,n):
        range_sum += vec[k]
        local_max = max(local_max,range_sum)
        if range_sum < 0:
            i+=k
            break
        
        

    ans = max(ans, local_max)
    i+=1

print(ans)