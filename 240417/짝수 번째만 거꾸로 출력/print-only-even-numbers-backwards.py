string = input().rstrip()

tmp = []
for idx, st in enumerate(string):
    idx +=1
    if idx % 2 == 0:
        tmp.append(st)
tmp.reverse()

print(''.join(tmp))