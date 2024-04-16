n = int(input())

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