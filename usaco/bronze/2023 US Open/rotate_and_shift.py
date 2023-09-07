n, k, t = list(map(int, input().split()))
res = list(range(0, n))
active = list(map(int, input().split()))


def rotate_active():
    global active
    for i in range(0, k):
        active[i] = (active[i]+1)%n


def rotate():
    global res
    temp = res[active[-1]]
    for i in range(0, k):
        t = res[active[i]]
        res[active[i]] = temp
        temp = t


for _ in range(0, t):
    rotate()
    rotate_active()

print(' '.join(list(map(str, res))))


