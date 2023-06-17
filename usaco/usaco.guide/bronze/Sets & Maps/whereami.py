"""
ID: neel.pa1
LANG: PYTHON3
TASK: whereami
"""

file_in = open("whereami.in", "r")
file_out = open("whereami.out", "w")

n = int(file_in.readline())
m = file_in.readline()


def calculate_smallest_k(mailboxes):
    for k in range(1, n + 1):
        substrings = set()
        for i in range(n - k + 1):
            substring = mailboxes[i:i + k]
            if substring in substrings:
                break
            substrings.add(substring)
        else:
            return k


print(calculate_smallest_k(m), file=file_out)

