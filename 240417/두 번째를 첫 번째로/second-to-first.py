string = input().rstrip()

target = string[1]
changed = string[0]

ans = ''
for ch in string:
    if ch == target:
        ans+=changed
    else:
        ans+=ch
print(ans)