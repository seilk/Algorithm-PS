import sys
from collections import deque

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def b_f(start, st_earn, end, N):
	INF = float("inf")
	dist = [INF] * N
	dist[start] = -st_earn
	for n in range(N - 1):
		for i in range(N):
			if dist[i] == INF: continue
			for p, d in grp[i]:
				if dist[p] > d + dist[i] - earn[p]:
					dist[p] = d + dist[i] - earn[p]

	# 음의 cycle 체크 : v번째 loop를 통해서 값의 변화가 있는지 없는지 판단.
	for i in range(N):
		for p, d in grp[i]:
			if dist[p] > d + dist[i] - earn[p]:
				if findRoute(i, p, end): # 값의 변화가 존재하는 노드에서 도착점으로 갈 수 있는지 판단.
					return False, dist
	return True, dist


def findRoute(i, p, end):
	dq = deque([i, p])
	vist = [0] * N
	while dq:
		cur = dq.popleft()
		if vist[cur] == 1 : continue
		if cur == end : return True
		vist[cur] = 1
		for nxt, d in grp[cur]:
			if vist[nxt] == 1 : continue
			dq.append(nxt)
	return False

def init():
	N, start, end, M = MIS()
	grp = [[] for i in range(N)]
	for m in range(M):
		s, e, d = MIS()
		grp[s].append((e, d))
	earn = [*MIS()]
	return N, grp, earn, start, end


N, grp, earn, start, end = init()
flg, dist = b_f(start, earn[start], end, N)
if flg == False:
	print("Gee")
else:
	print(-dist[end] if dist[end] != float("inf") else "gg")

# 4 0 3 4
# 0 1 0
# 1 2 0
# 2 1 0
# 0 3 10
# 10 10 10 10
# output = 10


# 4 1 3 4
# 0 1 0
# 1 2 0
# 2 1 0
# 0 3 10
# 10 10 10 10
# output = gg

# 3 0 2 4
# 0 1 9999
# 1 2 9999
# 1 1 9999
# 0 2 0
# 10000 10000 10000
# output = Gee

# 5 0 4 6
# 0 1 10000
# 1 2 0
# 2 1 0
# 1 3 0
# 0 3 0
# 3 4 0
# 0 0 1 0 0
# output = Gee
