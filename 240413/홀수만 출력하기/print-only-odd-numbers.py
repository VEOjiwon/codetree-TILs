N = int(input())
nums = list(int(input()) for _ in range(N))

for num in nums:
    if num % 2 == 1 and num % 3 ==0:
        print(num)