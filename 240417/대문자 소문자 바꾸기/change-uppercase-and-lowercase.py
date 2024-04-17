string = input().rstrip()

for ch in string:
    if ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch.lower(),end='')