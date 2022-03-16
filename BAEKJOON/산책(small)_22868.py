import sys
from collections import deque

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def init():
	N, M = MIS()
	grp = [[] for i in range(N + 1)]
	for m in range(M):
		u, v = MIS()
		grp[u].append(v)
		grp[v].append(u)
	s, e = MIS()
	for i in range(1, N + 1):
		grp[i].sort()
	return N, M, grp, s, e


def bfs(s, e):
	dq = deque([[s, 0, [s]]])
	vist = [0] * (N + 1)
	vist[s] = 1
	while dq:
		cur, dis, root = dq.popleft()
		if cur == e:
			return root, dis
		for nxt in grp[cur]:
			if vist[nxt] == 1: continue
			vist[nxt] = 1
			dq.append([nxt, dis + 1, root + [nxt]])


def bfs2(e, s):
	dq = deque([[e, 0, [e]]])
	vist = [0] * (N + 1)
	vist[e] = 1
	while dq:
		cur, dis, root = dq.popleft()
		if cur == s:
			return root, dis
		for nxt in grp[cur]:
			if vist[nxt] == 1: continue
			if banned[nxt] == 1: continue
			vist[nxt] = 1
			dq.append([nxt, dis + 1, root + [nxt]])


N, M, grp, s, e = init()
flg = False
rootStoE, distStoE = bfs(s, e)

banned = [0] * (N + 1)
for node in rootStoE:
	if node == s : continue
	banned[node] = 1

vist = [0] * (N + 1)
vist[e] = 1
flg = False
rootEtoS, distEtoS = bfs2(e, s)

print(distStoE + distEtoS)


'''
4 5
3 4
3 1
2 1
3 2
4 2
1 4
'''