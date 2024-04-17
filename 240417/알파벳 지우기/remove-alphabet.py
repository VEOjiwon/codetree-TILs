string1 = input().rstrip()
string2 = input().rstrip()

arr1 = []
for ch in string1:
    if ch.isalpha():
        continue
    arr1.append(ch)

arr2 = []
for ch in string2:
    if ch.isalpha():
        continue
    arr2.append(ch)

print(int(''.join(arr1)) + int(''.join(arr2)))