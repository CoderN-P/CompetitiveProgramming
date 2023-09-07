nums = sorted(list(map(int, input().split())))


def find():
    for a in range(0, 6):
        for b in range(0, 6):
            if a == b:
                continue
            for c in range(0, 6):
                if c == a or c == b:
                    continue
                a1, b1, c1 = nums[a], nums[b], nums[c]
                if a1 + b1 + c1 == nums[-1]:
                    print(a1, b1, c1)
                    return


find()
