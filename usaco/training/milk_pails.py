"""
ID: neel.pa1
LANG: PYTHON3
TASK: pails
"""

file_in = open("pails.in", "r")
file_out = open("pails.out", "w")

one, two, total = list(map(int, file_in.readline().split()))

def dfs(cur):
    if cur + max(one, two) > total:
        if cur + min(one, two) > total:
            return cur
        else:
            return cur + min(one, two)

    else:
        return max(dfs(cur + one), dfs(cur + two))

file_out.write(str(dfs(0)) + "\n")