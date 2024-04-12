age1, s1 = input().split()
age2, s2 = input().split()

if (int(age1) >= 20 and s1=='M') or (int(age2) >= 20 and s2=='M'):
    print(1)
else:print(0)