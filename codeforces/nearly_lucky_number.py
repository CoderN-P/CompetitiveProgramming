res = input()

n = str(res.count('4') + res.count('7'))

if '4' in n or '7' in n:
    print('YES')
else:
    print('NO')

