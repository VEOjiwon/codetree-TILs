arr = list(input())

def convert_decimal(arr):
    num = 0
    for j in range(len(arr)):
        num += (2**(len(arr)-j-1))*int(arr[j])
    return num
    
ans = 0

for i in range(len(arr)):
    if arr[i] == '0':
        arr[i] ='1'
        num = convert_decimal(arr)
        ans = max(ans, num)
        arr[i] = '0'
    elif arr[i] == '1':
        arr[i] ='0'
        num = convert_decimal(arr)
        ans = max(ans, num)
        arr[i] = '1'
        

print(ans)