s = input()
res = ''
skip = False
for i in range(0, len(s)):
    if skip:
        skip = False
        continue

    if s[i] == '.':
        res += '0'

    if s[i] == '-':
        if s[i+1] == '-':
            res += '2'
        elif s[i+1] == '.':
            res += '1'
        skip = True

print(res)



