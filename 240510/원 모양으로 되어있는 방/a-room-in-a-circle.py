import sys
n = int(input())
rooms = list(int(input()) for _ in range(n))

ans = sys.maxsize
for i in range(len(rooms)):
    tot_cost = 0
    for j in range(len(rooms)):
        cost = 0
        if j > i:
            cost = j - i
        elif j < i:
            cost = n - (i - j)
        else:
            continue
        tot_cost += cost * rooms[j]
    ans = min(ans, tot_cost)
    
print(ans)