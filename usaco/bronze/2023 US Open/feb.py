n = int(input())
s = input()

# Step 1, calculate original excitement

excitement = 0
f = []
for i in range(1, n):
    if s[i] == s[i-1]:
        excitement += 1

for i in range(0, n):
    v = s[i]
    if v == 'F':

        if i > 0 and i < n-1:
            a = ["E", "B"]
            b = s[i-1] in a and s[i+1] in a

            if s[i-1] == s[i+1] and b:
                f.append((0, 2))
            elif s[i-1] != s[i+1] and b:
                f.append(1)
            elif s[i-1] == "F" and s[i+1] in a or s[i+1] == "F" and s[i-1] in a:
                f.append((1, 2))
            elif s[i-1] == "F" and s[i+1] == "F":
                f.append((0, 1, 2))
        else:
            f.append((0, 1))


print(f)







