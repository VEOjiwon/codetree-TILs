a, b = map(float,input().split())
b = int(b)
if a.is_integer() and a>=1:
    for _ in range(b):
        print(int(a),end='')