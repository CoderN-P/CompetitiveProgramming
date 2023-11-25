t = int(input())

for _ in range(0, t):
    s = input()
    if s[0] == 'a':
        print('YES')
        continue
    elif s[0] == 'b':
        if s[1] == 'a':
            print('YES')
            continue
    else:
        if s[2] == 'a':
            print('YES')
            continue
    print('NO')
