import sys
from collections import deque
from heapq import heapify, heappop, heappush

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def init():
	n, d, start = MIS()
	grp = [[] for i in range(n + 1)]
	time = [float("inf")] * (n + 1)
	for _ in range(d):
		a, b, w = MIS()
		grp[b].append((a, w))  # b->a : b가 감염되면 a가 w 만에 감염된다
	return grp, time, start

def bfs(start, time):
	dq = [(0, start)]
	heapify(dq)
	while dq:
		t, cur = heappop(dq)
		if time[cur] < t : continue
		time[cur] = t
		for nxt, tt in grp[cur]:
			if time[nxt] <= t + tt: continue
			time[nxt] = t + tt
			heappush(dq, (t+tt, nxt))
	return sum([1 for i in time if i < float("inf")]), max(i for i in time if i < float("inf"))

t = int(In())
for _ in range(t):
	grp, time, start = init()
	print(*bfs(start, time))