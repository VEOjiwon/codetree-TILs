arr = list(input())

def convert_decimal(arr):
    arr.reverse()
    num = 0
    for i in range(len(arr)):
        num += ((i)**2)*int(arr[i])
    return num
ans = convert_decimal(arr)
for i in range(len(arr)):
    if arr[i] == '0':
        arr[i] ='1'
        num = convert_decimal(arr)
        ans = max(ans, num)
        arr[i] = '0'
print(ans)