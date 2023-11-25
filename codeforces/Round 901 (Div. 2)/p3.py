t = int(input())


def min_operations_to_divide_apples(n, m):
    if n % m != 0:
        return -1  # It's impossible to divide the apples equally

    def divide(apples, people, operations):
        if people == 1:
            return operations  # No more divisions needed for the last person

        # Find the largest power of 2 that can be used for division
        largest_power_of_2 = 1
        while largest_power_of_2 * 2 <= apples:
            largest_power_of_2 *= 2

        # Divide the apples and update the count and operations
        divided_apples = apples - largest_power_of_2
        return divided_apples + divide(largest_power_of_2, people - 1, operations + 1)

    return divide(n, m, 0)


for _ in range(0, t):
    n, m = list(map(int, input().split()))
    print(min_operations_to_divide_apples(n, m))

