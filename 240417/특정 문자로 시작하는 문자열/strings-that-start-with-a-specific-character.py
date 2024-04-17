n = int(input())
strings = list(input().strip() for _ in range(n))
target = input().rstrip()
cnt = 0
summed = 0
for st in strings:
    if st[0] == target:
        cnt+=1
        summed += len(st)
avg = summed / cnt
print(f'{cnt} {avg:.2f}')