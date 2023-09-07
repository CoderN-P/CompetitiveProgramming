probabilities = [1/70, 1/100, 1/300, 1/1200, 1/40000, 1/200, 1/10000, 1/500, 1/150, 1/600, 1/700, 1/450]

# Calculate the complementary probability
not_winning_prob = 1
for p in probabilities:
    not_winning_prob *= (p)

# Calculate the probability of winning at least one giveaway
winning_at_least_one_prob = 1 - not_winning_prob

print("Probability of winning at least one giveaway:", winning_at_least_one_prob)