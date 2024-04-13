n = int(input())

cmd = list(list(input().split()) for _ in range(n))

ranks = {'A':0, 'B':0}
cur = 'AB'
cnt = 0
for i in range(n):
    p, num = cmd[i]
    num = float(num)
    
    ranks[p] += num
    if ranks['A'] > ranks['B'] and (cur=='B' or cur =='AB'):
        cur = 'A'
        cnt+=1
    elif ranks['A'] < ranks['B'] and (cur=='A'or cur =='AB'):
        cur = 'B'
        cnt+=1
    elif ranks['A'] == ranks['B'] and (cur !='AB'):
        cur ='AB'
        cnt+=1
            
print(cnt)