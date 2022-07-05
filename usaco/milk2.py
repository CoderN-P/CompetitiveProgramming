"""
ID: neel.pa1
LANG: PYTHON3
TASK: milk2
"""

file_in = open("milk2.in", "r")
file_out = open("milk2.out", "w")


def is_overlaping(a, b):
    if b[0] > a[0] and b[0] <= a[1]:
        return True
    else:
        return False


def merge(arr):
    # sort the intervals by its first value
    arr.sort(key=lambda x: x[0])

    merged_list = []
    merged_list.append(arr[0])
    for i in range(1, len(arr)):
        pop_element = merged_list.pop()
        if is_overlaping(pop_element, arr[i]):
            new_element = pop_element[0], max(pop_element[1], arr[i][1])
            merged_list.append(new_element)
        else:
            merged_list.append(pop_element)
            merged_list.append(arr[i])
    return merged_list


cow_amt = int(file_in.readline().strip())
cows = [list(map(int, file_in.readline().split())) for _ in range(0, cow_amt)]
cows = merge(cows)
if len(cows) == 1:
    time_in_between = 0
    longest_time = cows[0][1] - cows[0][0]
else:
    time_in_between = max([cows[n][0] - cows[n - 1][1] for n in range(1, len(cows))])
    longest_time = max([cow[1] - cow[0] for cow in cows])

file_out.write(f'{longest_time} {time_in_between}\n')