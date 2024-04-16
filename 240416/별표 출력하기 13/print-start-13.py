n = int(input())

if n == 1:
    print('*')
    print('*')
elif n == 2:
    print('* * ')
    print('*')
    print('*')
    print('* * ')
else:
    for i in range(n,1,-1):
        print('* '*i)
        if i ==2:
            continue
        print('*')

    for i in range(2,n+1):
        print('* '*i)
        if i ==n:
            continue
        print('*')