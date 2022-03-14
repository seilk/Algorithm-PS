import sys
from heapq import heappush, heappop
In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def init():
	N, M, K = MIS()
	grp = [[] for i in range(N + 1)]
	for m in range(M):
		u, v, t = MIS()
		grp[u].append((v, t))
		grp[v].append((u, t))
	vist = [-1] * (N + 1)
	return grp, vist, N, K


def dijk(k):
	global ans
	pq = []
	dist = [[float("inf")] * (k + 1) for i in range(N + 1)]
	heappush(pq, (0, 1, 0))
	while pq:
		t, node, pj = heappop(pq)
		if dist[node][pj] < t: continue
		dist[node][pj] = t
		for nxt, tt in grp[node]:
			if dist[nxt][pj] > t + tt:
				dist[nxt][pj] = t + tt
				heappush(pq, (t + tt, nxt, pj))
			if pj < k and dist[nxt][pj+1] > t:
				dist[nxt][pj+1] = t
				heappush(pq, (t, nxt, pj + 1))
	return min(dist[N])


grp, vist, N, k = init()
vist[1] = 1
print(dijk(k))
