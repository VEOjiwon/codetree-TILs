n = int(input())
nums = list(map(int, input().split()))

cost = 0
for _ in range(n//2):
    nums.sort()
    cost += nums[0] + nums[1]
    nums.append(nums[0]+nums[1])
    nums = nums[2:]
    

cost += sum(nums)
print(cost)