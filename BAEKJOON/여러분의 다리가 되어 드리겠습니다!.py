import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

n = int(In())

grp = [[] for i in range(n+1)]
for _ in range(n-2):
	u, v = MIS()
	grp[u].append(v)
	grp[v].append(u)

dq = deque([1])
vist = [0] * (n + 1)
while dq:
	cur = dq.popleft()

	for nxt in grp[cur]:
		if vist[nxt] == 1: continue
		vist[nxt] = 1
		dq.append(nxt)

for i in range(1, n+1):
	if vist[i] == 0:
		if i > 1:
			print(1, i)
			break
