string = input().rstrip()
cmd = input().rstrip()
string = list(string)
for c in cmd:
    if c == 'L':
        string.append(string[0])
        string.pop(0)
    elif c == 'R':
        string = [string[-1]] + string
        string.pop(-1)
print(''.join(string))