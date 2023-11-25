correct = [input() for _ in range(3)]
guess = [input() for _ in range(3)]
taken = [[False for _ in range(0, 3)] for _ in range(0, 3)]
green, yellow = 0, 0
for row in range(0, 3):
    for col in range(0, 3):
        if guess[row][col] == correct[row][col]:
            green += 1
            taken[row][col] = True
        else:
            for row1 in range(0, 3):
                for col1 in range(0, 3):
                    if row1 == row and col1 == col:
                        continue
                    if correct[row1][col1] == guess[row][col] and correct[row1][col1] != guess[row1][col1] and not taken[row1][col1]:
                        yellow += 1
                        taken[row1][col1] = True


print(green)
print(yellow)