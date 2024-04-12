n = int(input())

cnt = 1
i=1
while True:
    if n//i <= 1:
        break
    n = n // i
    cnt+=1
    i+=1
    
    

print(cnt)