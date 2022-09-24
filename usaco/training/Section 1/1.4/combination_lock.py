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
perms = 0
char_count = [0] * n


def search(curr):
	global perms
	if len(curr) == 3:
		a = []
		b = []
		for j, c in enumerate(curr):
			a.append(abs(fj_combo[j]-c))
			b.append(abs(m_combo[j]-c))
		if all([a1<=2 or (n-a1)<=2 for a1 in a]) or all([b1<=2 or (n-b1)<=2 for b1 in b]):
			perms += 1

		return
	for i in range(1, n + 1):
		curr1 = curr.copy()
		curr1.append(i)
		search(curr1)



search([])
file_out.write(str(perms)+'\n')
