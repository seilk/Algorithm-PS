import sys
from heapq import heappop, heappush

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
n, m, x = MIS()

grp = [ [ ] for i in range(n+2) ]
grpRev = [ [ ] for i in range(n+1) ]

def dijk(start, n, grp) :
	INF = float("inf")
	hq = [ ]
	dist = [ INF for i in range(n+1) ]
	dist[ start ] = 0
	heappush(hq, (0, start))

	while hq :
		d, cur = heappop(hq)
		if dist[ cur ]<d : continue
		dist[ cur ] = d
		for dd, nxt in grp[ cur ] :
			if dist[ nxt ]<dd+d : continue
			heappush(hq, (dd+d, nxt))

	return dist

for _ in range(m) :
	u, v, d = MIS()
	grp[ u ].append((d, v))
	grpRev[ v ].append((d, u))

dist = dijk(x, n, grp)
distRev = dijk(x, n, grpRev)

print(max([ a+b for a, b in zip(dist, distRev) if a != float("inf") and b != float("inf")]))
