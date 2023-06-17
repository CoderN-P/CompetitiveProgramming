"""
ID: neel.pa1
LANG: PYTHON3
"""

n = int(input())
c = sorted(list(map(int, input().split())))
mx_price = [0, 0]
for i in range(0, n):
    if c[i] == mx_price[0]:
        pass
    elif c[i]*(n-i) > mx_price[1]:
        mx_price = [c[i], c[i]*(n-i)]

print(str(str(mx_price[1])+' '+str(mx_price[0])))



