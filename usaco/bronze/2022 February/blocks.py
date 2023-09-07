n = int(input())
blocks = [input() for _ in range(0, 4)]
words = [input() for _ in range(0, n)]

for word in words:
    blockMap = []
    for i in range(0, 4):
        block = blocks[i]
        blockMap.append([])
        for c in range(0, len(word)):
            if word[c] in block:
                blockMap[i].append(word[c])
    for c in word:




    if sorted(blockMap) == list(range(0, len(word))):
        print('YES')
    else:
        print('NO')
