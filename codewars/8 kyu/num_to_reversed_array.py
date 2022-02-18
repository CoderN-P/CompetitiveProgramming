def digitize(n):
    return list(map(int, list(str(n)[::-1])))