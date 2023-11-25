t = int(input())
res = []


for _ in range(0, t):
    num = int(input())
    ans_prev = -1
    ans = 0
    idx = 1
    while ans > ans_prev:
        n = num - idx - 1
        s = (n)*(n+1)*(2*n+1)//6
        m = 0
        cur_idx = n + 1
        for i in range(num, n, -1):
            v = i*cur_idx
            m = max(m, v)
            s += v
            cur_idx += 1
        ans_prev = ans
        ans = s - m
        idx += 1

    res.append(ans_prev)

for i in res:
    print(i)

 '''
    while cur > 0:
        if len(x) > 0:
            if a - cur >= x[0]:
                cur += x.pop(0)
            if x[0] > a and cur == 1:
                cur = a
                x.pop(0)

        cur -= 1
        total += 1
    '''