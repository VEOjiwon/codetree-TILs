import sys

N, weight = map(int, sys.stdin.readline().split())
dia = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

total_weight = 0
total_val = 0
for idx, (w, v) in enumerate(dia):
    dia[idx].append(v/w)
dia.sort(key=lambda x: (x[2]),reverse=True)

for w, v, _ in dia:
    
    total_weight+=w
    if  total_weight > weight:
        total_val += (w - (total_weight - weight)) / w * v
        break
    if total_weight == weight:
        total_val += v
        break
    total_val += v

print('%.3f'%total_val)