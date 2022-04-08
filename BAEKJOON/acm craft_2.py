import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())


t = int(In())
for _ in range(t):
	n, k = MIS()
	grp = [[] for i in range(n + 1)]
	completeTime = [0] + [*MIS()]
	times = [[0] for i in range(n + 1)]
	indeg = [0] * (n + 1)
	for __ in range(k):
		u, v = MIS()
		grp[u].append(v)
		indeg[v] += 1

	target = int(In())

	queue = deque([])
	for i in range(1, n + 1):
		if indeg[i] == 0:
			queue.append(i)

	ans = [0] * (n + 1)
	while queue:
		cur = queue.popleft()
		ans[cur] = completeTime[cur] + max(times[cur])
		if cur == target :
			break
		for nxt in grp[cur]:
			times[nxt].append(ans[cur])
			indeg[nxt] -= 1
			if indeg[nxt] == 0:
				queue.append(nxt)

	print(ans[target])
