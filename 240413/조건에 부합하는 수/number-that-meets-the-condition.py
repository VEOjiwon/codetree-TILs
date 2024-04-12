a = int(input())

res= 0
for i in range(1,a+1):
    tmp = i // 8
    ttmp = i % 7
    if (i % 2 !=0 or i % 4 ==0) and tmp % 2 != 0 and ttmp >=4:    
        print(i, end=' ')