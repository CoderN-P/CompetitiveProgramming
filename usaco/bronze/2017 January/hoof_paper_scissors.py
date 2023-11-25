fin = open('hps.in', 'r')
fout = open('hps.out', 'w')
n = int(fin.readline())
games = [list(map(int, fin.readline().split())) for _ in range(0, n)]
ans = 0
m = ['H', 'P']
for permutations in [['H', 'P', 'S'], ['H', 'S', 'P'], ['P', 'H', 'S'], ['H', 'S', 'P'], ['S', 'H', 'P'],
                     ['S', 'P', 'H']]:
    a_score = 0
    for o, t in games:
        a, b = permutations[o-1], permutations[t-1]

        if a == 'H' and b == 'S':
            a_score += 1
        elif b == 'P' and a == 'S':
            a_score += 1
        elif b == 'H' and a == 'P':
            a_score += 1

    ans = max(ans, a_score)

fout.write(str(ans))
