t = int(input())
res = []




def solve(a):
    n = len(a)
    operations = []

    # Helper function to perform an operation and update the array
    def perform_operation(l, r):
        s = 0
        for i in range(l, r + 1):
            s ^= a[i]
        for i in range(l, r + 1):
            a[i] = s

    # Initialize a DP table to keep track of operations
    dp = [[-1] * n for _ in range(9)]
    dp[0] = list(range(n))

    # DP to find a sequence of operations that results in all elements being 0
    for k in range(1, 9):
        for i in range(n):
            for j in range(i, n):
                if dp[k - 1][j] == -1:
                    continue
                current_xor = 0
                for x in range(i, j + 1):
                    current_xor ^= a[x]
                if dp[k - 1][j] ^ current_xor == 0:
                    dp[k][i] = j

    # Reconstruct the sequence of operations
    k = 8
    i = 0
    while k > 0:
        j = dp[k][i]
        if j == -1:
            return None  # No solution found
        operations.append((i + 1, j + 1))
        perform_operation(i, j)
        i = j + 1
        k -= 1

    return operations

# Example usage:


for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))

        operations = solve(a)
        for op in operations:
            print(op)









