n = int(input())

cur = ord('A')
for i in range(1,n+1):
    print('  '*(i-1), end='')
    for j in range(n-i+1):
        print(chr(cur), end =' ')
        cur+=1
        if cur == ord('Z')+1:
            cur = ord('A')
    print()