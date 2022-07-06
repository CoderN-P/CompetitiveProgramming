"""
ID: neel.pa1
LANG: PYTHON3
TASK: namenum
"""
acceptable_names = open("dict.txt", 'r')

file_in = open("namenum.in", "r")
file_out = open("namenum.out", "w")
mapping = {
    "2": ["A", "B", "C"], "5": ["J", "K", "L"], "8": ["T", "U", "V"],
    "3": ["D", "E", "F"], "6": ["M", "N", "O"], "9": ["W", "X", "Y"],
    "4": ["G", "H", "I"], "7": ["P", "R", "S"]
}
cow_id = file_in.readline().strip()
names = []

while line := acceptable_names.readline().strip():
    allowed = True

    if len(line) == len(cow_id):
        for i, n in enumerate(cow_id):
            if line[i] not in mapping[n]:
                allowed = False
                break
        if allowed:
            names.append(line)
if not names:
    names.append('NONE')

file_out.write('\n'.join(names)+'\n')


