n = int(input())

locks = [int(input()) for _ in range(0, n)]


def dfs(cur, idx):

    if idx == len(locks):
        if cur%360 == 0:
            return True
        return False

    return dfs(cur-locks[idx], idx+1) or dfs(cur+locks[idx], idx+1)


if dfs(0, 0):
    print('YES')
else:
    print('NO')



