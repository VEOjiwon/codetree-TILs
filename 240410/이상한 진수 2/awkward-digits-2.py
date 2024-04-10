import sys

a = sys.stdin.readline().rstrip()
la = []
for c in a:
    la.append(int(c))
n = len(la)

max_val = -1
for i in range(n):
    if la[i] == 0:
        la[i] = 1
    else:
        la[i] = 0
    decimal = 0
    for k in range(n):
        decimal += la[n-k-1] * (2**(k))
    max_val = max(max_val, decimal)
    if la[i] == 0:
        la[i] = 1
    else:
        la[i] = 0
print(max_val)