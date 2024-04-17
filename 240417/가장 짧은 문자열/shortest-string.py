import sys
strings = list(input().strip() for _ in range(3))

max_len = -1
min_len = sys.maxsize

for i in range(3):
    min_len = min(len(strings[i]), min_len)
    max_len = max(max_len,len(strings[i]))

print(max_len - min_len)