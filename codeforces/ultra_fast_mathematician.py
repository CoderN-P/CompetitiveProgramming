n1 = input()
n2 = input()
res = ''

for i in range(0, len(n1)):
    res += str(int(n1[i]!=n2[i]))

print(res)