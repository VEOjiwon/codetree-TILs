import sys
a = input().strip()
li = []
for c in a:
    li.append(c)
a = li

max_val = -1
for i in range(len(a)):
    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'
    tmp = int(''.join(a))
    comp = 0
    for k in range(0,len(a)):
        comp += int(a[len(a)-i-1]) * (k**2)
    if comp >= max_val:
        max_val = comp
print(max_val)