j = input()
le = len(j)
year = int(j)


def digits(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = n // 10
    return l


while True:
    year += 1
    if len(set(digits(year))) == le:
        break

print(year)
