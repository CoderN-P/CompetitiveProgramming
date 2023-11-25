print(0^0)
t = int(input())
res = []

for _ in range(0, t):
    n = int(input())
    binary_string = input()
    intV = int(binary_string, 2)
    result = [0 for _ in range(0, n+1)]
    result[binary_string.count('1')] = 1
    result[binary_string.count('0')] = 1

    for numOnes in range(0, n+1):

