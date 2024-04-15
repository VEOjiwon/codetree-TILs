n = int(input())
i=n
j=0
while i >=1:
    print('*'*i, end='')
    print(' '*(j),end='')
    print('*'*i)
    i-=1
    j+=2