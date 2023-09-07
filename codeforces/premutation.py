t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    permutations = [input() for _ in range(0, n)]
    start = None
    in_question = []
    for row in range(1, n):
        if permutations[row][0] == permutations[row-1][0]:
            start = permutations[row][0]
        elif row == n-1 and permutations[row][0] == permutations[0][0]:
            start = permutations[row][0]
        else:
            in_question.append(permutations[row])
            in_question.append(permutations[row-1])

    if in_question[0][0] == start:
        res.append(start+' '+in_question[1])
    else:
        res.append(start+' '+in_question[0])

for i in res:
    print(i)