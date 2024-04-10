import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
cost = 0
for i in range(n//2):
    val = nums[0] + nums[1]
    cost += val
    nums = nums[2:]
    for j in range(len(nums)):
        if nums[j] <= val:
            nums.insert(j,val)
            break
    

cost += sum(nums)
print(cost)