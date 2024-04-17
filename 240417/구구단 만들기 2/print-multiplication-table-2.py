a, b = map(int, input().split())
num = a

for i in range(1,b+1):
    for j in range(b,a-1,-1):
        if j == a:
            print(j,'*',a*i,'=',j*a*i, end ='')
        else:
            print(j,'*',a*i,'=',j*a*i, end =' / ')
    print()