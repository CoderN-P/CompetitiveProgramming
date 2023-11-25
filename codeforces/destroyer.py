t = int(input())

for _ in range(0, t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    lines = []

    for position in a:
        if position == 0:
            lines.append(0)
        else:
            for i in range(0, len(lines)):
                if lines[i] == position - 1:
                    lines[i] += 1
                    break
            else:
                print('NO')
                break
    else:
        print('YES')