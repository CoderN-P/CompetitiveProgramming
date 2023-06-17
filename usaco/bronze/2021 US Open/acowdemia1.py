"""
ID: neel.pa1
LANG: PYTHON3
TASK: acowdemia1
"""

n, l = list(map(int, input().split()))
papers = list(map(int, input().split()))


def calculate_h_index(papers):
    if len(papers) == 1:
        return 1 if papers[0] >= 1 else 0
    papers.sort()
    for n, i in enumerate(papers):
        if i + n >= len(papers):
            return papers[n - 1]


