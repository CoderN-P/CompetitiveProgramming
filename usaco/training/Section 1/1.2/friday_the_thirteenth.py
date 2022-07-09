"""
ID: neel.pa1
LANG: PYTHON3
TASK: friday
"""

file_in = open("friday.in", "r")
file_out = open("friday.out", "w")

years = int(file_in.readline())
days = {6: 0, 7: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
day = 1
for year in range(1900, 1900 + years):
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    leap = False
    if year % 400 == 0 and year % 100 == 0:
        leap = True

    elif year % 4 == 0 and year % 100 != 0:
        leap = True

    if leap:
        months[2] = 29

    for month, month_days in months.items():

        if month == 1 and year == 1900:
            day = 13 % 7
            days[day] += 1

        else:
            if month == 1:
                days_in_month = 31
            else:
                days_in_month = months[month - 1]

            day = (day + days_in_month) % 7
            if day == 0:
                day = 7
            days[day] += 1

file_out.write(" ".join(list(map(str, days.values()))) + "\n")
