arr = list(input())

def convert_decimal(arr):
    
    num = 0
    for i in range(len(arr)):
        num += ((len(arr)-i-1)**2)*int(arr[i])
    return num
    
ans = 0
for i in range(len(arr)):
    if arr[i] == '0':
        arr[i] ='1'
        num = convert_decimal(arr)
        ans = max(ans, num)
        arr[i] = '0'
    else:
        arr[i] ='0'
        num = convert_decimal(arr)
        ans = max(ans, num)
        arr[i] = '1'
print(ans)