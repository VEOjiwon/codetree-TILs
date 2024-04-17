from itertools import combinations
import sys
n = int(input())
arr = list(map(int, input().split()))

tmp = sys.maxsize
for comb in combinations(arr,2):
    diff = abs(comb[0] - comb[1])
    tmp = min(tmp,diff)
print(tmp)