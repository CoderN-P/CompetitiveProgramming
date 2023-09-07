n = int(input())
if n%2 == 1:
    print('-1')
else:
    print(' '.join(list(map(str, range(n, 0, -1)))))