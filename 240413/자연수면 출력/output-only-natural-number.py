a, b = map(float,input().split())
b = int(b)
if (a * 10 ) %10 ==0:
    for _ in range(b):
        print(int(a),end='')