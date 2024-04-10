import sys

n = int(sys.stdin.readline())
vec = list(map(int, sys.stdin.readline().split()))
ans = -1248000
    
range_sum = 0
local_max = -127000
for i in range(n):
    range_sum += vec[i]
    if local_max < range_sum:
        local_max = range_sum
    elif range_sum < 0:
        range_sum = 0

print(local_max)