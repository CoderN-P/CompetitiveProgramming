"""
ID: neel.pa1
LANG: PYTHON3
TASK: wormhole
"""


class Cord(object):
    """Instances of the wormhole instances"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paired = None

    def __repr__(self):  # for debugging # may be better to subclass from tuple
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def next(self):
        """
        Returns: the next wormhole the cow will encounter after jumping out of
            the current wormhole.
        """
        for d in cords:
            if d.y == self.y and d.x > self.x:
                return d
        return None


with open('wormhole.in', 'r') as fin:
    N = int(fin.readline())  # N in [2,12], 11! = 0.3M
    cords = []
    for i in range(N):
        x, y = map(int, fin.readline().split())
        cords.append(Cord(x, y))
    cords.sort(key=lambda c: c.x)  # would be easier were it subclass of tuple


def pair(c):
    """Pair the coordinates together.
    Parameter c: a tuple of the two coordinates to be paired together
    """
    c1, c2 = c[0], c[1]
    c1.paired = c2
    c2.paired = c1


def pairs(s):
    """Returns: all possible combinations of pairs in given coordinations."""
    l = list(s)

    if len(l) == 2:
        return [[(l[0], l[1])]]

    result = []
    i = 0
    for j in range(1, len(s)):
        rests = pairs(s - {l[i], l[j]})
        pair = [[(l[i], l[j])] + rest for rest in rests]
        result += pair
    return result


pl = pairs(set(cords))

count = 0  # more substantial name
for pairings in pl:
    for p in pairings:
        pair(p)

    loop = False  # hasLoop for bool
    for c in set(cords):
        route = set()  # list of entrances of wormhole visited

        while True:
            n = c.paired  # exit of wormhole
            if n in route:
                loop = True
                break
            route |= {n}
            if n.next() is None:  # no further wormholes to encounter # if not
                break
            else:
                c = n.next()

        if loop == True:  # if discovered a loop, no need to consider
            break
    if loop == True:
        count += 1

# print (count)

result = str(count)

# stop = timeit.default_timer()

# print (stop1-start)
# print (stop2-stop1)
# print (stop-stop2)

with open('wormhole.out', 'w') as fout:
    fout.write(result + '\n')