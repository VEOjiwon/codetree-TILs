n = int(input())
nums = list(map(int, input().split()))

nums.sort()
cost = 0
for i in range(n//2):
    val = nums[0] + nums[1]
    cost += val
    nums = nums[2:]
    for j in range(len(nums)):
        if nums[j] < val:
            nums.insert(j-1,val)

cost += sum(nums)
print(cost)