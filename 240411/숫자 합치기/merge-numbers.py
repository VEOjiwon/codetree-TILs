import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
cost = 0
tmp = nums[0] + nums[1]
cost += tmp
nums = nums[2:]
for i in range(len(nums)//2):
    if tmp < nums[1]:
        tmp += nums[0]
        cost = tmp + nums[0]
        nums = nums[1:]
    else:
        val = nums[0] + nums[1]
        tmp = val
        cost += val
        nums = nums[2:]
    
    
    

cost += sum(nums)
print(cost)