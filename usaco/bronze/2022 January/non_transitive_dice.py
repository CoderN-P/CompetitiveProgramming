t = int(input())


def beats(a, b):
    aScore = 0
    bScore = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i] > b[j]:
                aScore += 1
            if a[i] < b[j]:
                bScore += 1

    return aScore > bScore


def solve(a, b, ab, ba):
    for c in range(1, 11):
        for d in range(1, 11):
            for e in range(1, 11):
                for f in range(1, 11):
                    die = [c, d, e, f]
                    if beats(a, die) and ba and beats(die, b):
                        return 'yes'
                    if beats(b, die) and ab and beats(die, a):
                        return 'yes'

    return 'no'


for _ in range(t):
    a = list(map(int, input().split()))
    a, b = a[:4], a[4:]
    print(solve(a, b, beats(a, b), beats(b, a)))
