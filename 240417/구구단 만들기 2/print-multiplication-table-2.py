a, b = map(int, input().split())
num = 2

for i in range(4):
    for j in range(b,a-1,-1):
        if j == a:
            print(j,'*',num,'=',j*num, end ='')
        else:
            print(j,'*',num,'=',j*num, end =' / ')
    num +=2
    print()