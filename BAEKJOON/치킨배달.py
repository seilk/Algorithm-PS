import sys
from itertools import combinations

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

n, k = MIS()
town = [[*MIS()] for i in range(n)]

chicken = []
home = []
for i in range(n) :
	for j in range(n) :
		if town[i][j] == 2 :
			chicken.append((i, j))
		if town[i][j] == 1 :
			home.append((i, j))

candi = list(combinations(chicken, k))


MAX = float("inf")
ans = MAX
for cc in candi :
	dist = 0
	for hx, hy in home :
		hdist = MAX
		for cx, cy in cc:
			hdist = min(hdist, abs(hx - cx) + abs(hy - cy))
		dist += hdist
	ans = min(ans, dist)
print(ans)
