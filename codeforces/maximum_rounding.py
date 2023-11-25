t = int(input())

for _ in range(0, t):
    n = list(map(int, list(input())))
    for i in range(len(n)-1, -1, -1):
        if n[i] >= 5:
            if i == 0:
                n[i] = 1
                for j in range(len(n)-1, 0, -1):
                    n[j] = 0
            else:
                n[i-1] += 1
                for j in range(len(n)-1, i-1, -1):
                    n[i] = 0
                if n[i-1] == 10:
                    n[i-1] = 1
                    n.append(0)
    print(''.join(list(map(str, n))))



