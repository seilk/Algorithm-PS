import sys
from collections import deque
from copy import deepcopy
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def func(start, ans):
	dq = deque([(i, 0) for i in start]) # 노드, 시간
	vist = [0] * (N + 1)
	for n in start : vist[n] = 1; ans[n] = 0
	while dq:
		cur, t = dq.popleft()
		for nxt in grp[cur]:
			if not vist[nxt]:
				nei[nxt] += 1
				if nei[nxt] >= tot[nxt]/2:
					vist[nxt] = 1
					ans[nxt] = t + 1
					dq.append((nxt, ans[nxt]))
	print(*ans[1:])
	
N = int(In())
grp = [[] for i in range(N+1)]
tot = [0] * (N+1)
for i in range(1, N+1):
	info = [*MIS()]
	d = 0
	while info[d] != 0:
		grp[i].append(info[d])
		tot[i] += 1
		d += 1
nei = [0] * (N+1)

M = int(In())
start = [*MIS()]
ans = [-1] * (N+1)
func(start, ans)
