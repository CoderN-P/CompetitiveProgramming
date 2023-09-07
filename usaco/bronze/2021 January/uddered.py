alphabet = input()
heard = input()

memo = {alphabet[i]: i for i in range(0, len(alphabet))}
res = 0
for i in range(0, len(heard)):
    if i < len(heard)-1:
        if memo[heard[i]] >= memo[heard[i+1]]:
            res += 1
    else:
        res += 1

print(res)