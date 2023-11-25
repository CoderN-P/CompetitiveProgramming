t = int(input())

for _ in range(0, t):
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if k%2 == 0:
        if min(a) < max(b):
            v = min(a)
            a.remove(v)
            a.append(max(b))
            b.remove(max(b))
            b.append(v)
        if min(b) < max(a):
            v = min(b)
            b.remove(v)
            a.append(v)
            b.append(max(a))
            a.remove(max(a))
    else:
        if min(a) < max(b):
            v = min(a)
            a.remove(v)
            a.append(max(b))
            b.remove(max(b))
            b.append(v)
        if k > 1:
            if min(b) < max(a):
                v = min(b)
                b.remove(v)
                a.append(v)
                b.append(max(a))
                a.remove(max(a))
            if min(a) < max(b):
                v = min(a)
                a.remove(v)
                a.append(max(b))
                b.remove(max(b))
                b.append(v)
    print(sum(a))



