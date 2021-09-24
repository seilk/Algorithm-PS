import sys
from operator import itemgetter

n = int(sys.stdin.readline().rstrip())
coords = []
coord = []
for _ in range(n):
    coord = list(map(int, sys.stdin.readline().split()))
    coords.append(coord)
coords.sort(key = itemgetter(0, 1))
# coords.sort(key=lambda x: (x[0], x[1]))
for _ in range(n):
    print(*coords[_])


