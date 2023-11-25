t = int(input())
res = []

for _ in range(0, t):
    room_w, room_h = list(map(int, input().split()))
    x1, y1, x2, y2 = list(map(int, input().split()))
    w, h = list(map(int, input().split()))
    if ((x2 - x1) + w) > room_w and (y2-y1 + h) > room_h:
        res.append(-1)
        continue
    bl_b_x, bl_b_y, tr_b_x, tr_b_y = 0, 0, w, h

    # no overlap
    if x1 >= tr_b_x or x2 <= bl_b_x or y1 >= tr_b_y or y2 <= bl_b_y:
        res.append(0)
    else:
        if w + (x2-x1) > room_w:
            res.append(h-y1)
        elif h + (y2 - y1) > room_h:
            res.append(w-x1)
        else:
            res.append(min(h-y1, w-x1))

for i in res:
    print(i)