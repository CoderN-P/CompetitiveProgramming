white = list(map(int, input().split()))
black_1 = list(map(int, input().split()))
black_2 = list(map(int, input().split()))


def overlap_area(a, a2, b=False):
    if (a[3] <= a2[1]) or (a[1] >= a2[3]):
        return 0

    if (a[0] >= a2[2]) or (a[2] <= a2[0]):
        return 0

    if b:
        dx_max, dx_min = min(a[2], a2[2], white[2]),  max(a[0], a2[0], white[0])
        dy_max, dy_min = min(a[3], a2[3], white[3]), max(a[1], a2[1], white[1])
        if dx_max - dx_min <= 0:
            return 0
        if dy_max - dy_min <= 0:
            return 0

        return (dx_max - dx_min) * (
                    dy_max - dy_min)

    return (min(a[2], a2[2]) - max(a[0], a2[0])) * (min(a[3], a2[3]) - max(a[1], a2[1]))


a = (white[2] - white[0]) * (white[3] - white[1])

if overlap_area(white, black_1) + overlap_area(white, black_2) - overlap_area(black_1, black_2, b=True) >= a:
    print('NO\n')
else:
    print('YES\n')
