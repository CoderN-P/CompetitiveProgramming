fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n, t = list(map(int, fin.readline().split()))
teams = [list(map(int, fin.readline().split())) for _ in range(0, n)]
m = int(fin.readline())
words = [(fin.readline(), int(fin.readline())) for _ in range(0, m)]
d = [{i[0]: 0 for i in words} for _ in range(0, n)]
pts = [0 for _ in range(0, n)]
solved_words = [[] for _ in range(0, n)]
removed = []
player = 0
team = 0
while sum(pts) < m:
    if player == 0:
        a = teams[team][0]
        b = teams[team][3]
    else:
        a = teams[team][2]
        b = teams[team][1]

    time_remaining = t
    for i in range(0, len(words)):
        if i in removed:
            continue

        word, complexity = words[i]
        time_before = d[team][word]
        time_needed = max(1, complexity - (a + b) - time_before)
        if time_needed <= time_remaining:
            pts[team] += 1
            solved_words[team].append(word.strip())
            removed.append(i)
            time_remaining -= time_needed
            if time_remaining == 0:
                break
        else:
            d[team][word] += time_remaining
            words.append(words.pop(i))
            break
    team = (team + 1) % n
    if team == 0:
        if player == 0:
            player = 1
        else:
            player = 0

for i in range(0, n):
    fout.write(str(pts[i])+' '+' '.join(list(map(str, solved_words[i])))+'\n')
