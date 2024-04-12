cnt = 0
summed = 0
while True:
    n = int(input())
    if 20<=n<30:
        summed+=n
        cnt+=1
    else:
        ans = summed/cnt
        print(f'{ans:.2f}')
        break