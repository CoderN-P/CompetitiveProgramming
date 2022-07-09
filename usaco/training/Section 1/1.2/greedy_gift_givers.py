"""
ID: neel.pa1
LANG: PYTHON3
TASK: gift1
"""

import sys

file_in = open("gift1.in", "r")
file_out = open("gift1.out", "w")

people_amt = int(file_in.readline())

people = {}

for n in range(1, people_amt + 1):
    people[file_in.readline().strip()] = 0

for money in people.values():
    person = file_in.readline().strip()
    money = list(map(int, file_in.readline().split()))
    if money[1] == 0:
        continue
    money_per_person = money[0] // money[1]
    people[person] -= money[0] - (money[0] % money[1])
    for n in range(0, money[1]):
        reciever = file_in.readline().strip()
        people[reciever] += money_per_person
s = ""
for person, money in people.items():
    s += f"{person} {money}\n"

file_out.write(s)
