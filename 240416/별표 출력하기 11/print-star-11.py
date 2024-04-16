n = int(input())

num = 2 * n + 1

for i in range(num):
    for j in range(num):
        if j == 0 or i==0 or i == num-1 or j == num-1 or i % 2 == 0 or j % 2 == 0:
            print('* ',end='')

        else: print('  ',end='')
    print()