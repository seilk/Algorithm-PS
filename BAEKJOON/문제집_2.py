import sys
from heapq import heappush, heappop

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

n, m = MIS()

indeg = [0] * (n + 1)
grp = [[] for i in range(n + 1)]
for _ in range(m):
	u, v = MIS()
	indeg[v] += 1
	grp[u].append(v)

hq = [] # 최소힙
for i in range(1, n + 1):
	if indeg[i] == 0 :
		heappush(hq, i)

ans = []
while hq:
	node = heappop(hq)
	ans.append(node)

	for nxt in grp[node]:
		indeg[nxt] -= 1
		if indeg[nxt] == 0 :
			heappush(hq, nxt)

print(*ans)



"""
5 3
1 2
3 4
1 5
"""