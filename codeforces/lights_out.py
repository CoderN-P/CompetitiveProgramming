grid = [input().split() for _ in range(0, 3)]

new = [[1 for _ in range(0, 3)] for _ in range(0, 3)]


def toggle(s):
    if s == 1:
        return 0
    return 1


for i in range(0, 3):
    for j in range(0, 3):
        v = grid[i][j]
        if int(v) % 2 == 1:
            new[i][j] = toggle(new[i][j])
            if i != 2:
                new[i + 1][j] = toggle(new[i + 1][j])
            if i != 0:
                new[i-1][j] = toggle(new[i-1][j])

            if j != 2:
                new[i][j+1] = toggle(new[i][j+1])
            if j != 0:
                new[i][j-1] = toggle(new[i][j-1])


print(''.join(list(map(str, new[0])))+'\n'+''.join(list(map(str, new[1])))+'\n'+''.join(list(map(str, new[2]))))