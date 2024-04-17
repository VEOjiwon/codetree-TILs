str1 = list(input().strip().split())
str2 = list(input().strip().split())

str1.extend(str2)
print(''.join(str1))