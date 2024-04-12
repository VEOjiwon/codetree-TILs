a = int(input())
li = list(map(int, input().split()))

for l in li:
    print(1 if a > l else 0)