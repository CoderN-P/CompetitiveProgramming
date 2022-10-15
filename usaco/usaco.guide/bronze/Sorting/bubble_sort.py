size = int(input())
arr = list(map(int, input().split()))

swaps = 0

for _ in range(size):
    for j in range(0, size-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
print(f'Array is sorted in {swaps} swaps.\nFirst Element: {arr[0]}\nLast Element: {arr[-1]}')

