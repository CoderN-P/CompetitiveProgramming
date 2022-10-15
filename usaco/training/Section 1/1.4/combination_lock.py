"""
ID: neel.pa1
LANG: PYTHON3
TASK: combo
"""
file_in = open('combo.in', 'r')
file_out = open('combo.out', 'w')
n = int(file_in.readline())
fj_combo = list(map(int, file_in.readline().split()))
m_combo = list(map(int, file_in.readline().split()))
if n < 5:
	result = n**3
else:
	result = 250
	j = []
	for a, b in zip(fj_combo, m_combo):
		a_diff = abs(b - a)
		if a_diff <= 4 or a_diff >= (n - 4):
			j.append(max((5-(abs(a-b))), (5-n+a_diff)))
	result -= j[0]*j[1]*j[2] if len(j) != 0 else 0
file_out.write(str(result)+'\n')

