import sys

sys.setrecursionlimit(10 ** 5)

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def init(V, E):
	grp = [[] for i in range(V + 1)]
	for e in range(E):
		u, v, d = MIS()
		grp[u].append((v, d))
		grp[v].append((u, d))
	f1, f2 = MIS()
	vist = [0] * (V + 1)
	ans = -1
	left = 0
	right = int(1e9)
	return grp, f1, f2, vist, ans, left, right


def dfs(cur, f2, lmt):
	global mxx
	if cur == f2:
		return True
	for nxt, d in grp[cur]:
		if not vist[nxt] and d >= lmt:
			vist[nxt] = 1
			if dfs(nxt, f2, lmt):
				return True


V, E = MIS()
grp, f1, f2, vist, ans, left, right = init(V, E)

'''
1. 최장거리는 다익스트라로 구할 수 없다. (무한 루프) dist = [~~~~~~] 벨만 - 포드
2. DFS, BFS는 한번 방문한 노드를 다시 방문하지 않는다. -> 일부 경로에 대한 가능성을 맘대로 소멸 시키는 코드
3. 문제를 분리해서 생각 : 경로를 걸으면서 최고중량을 찾는다 X, 최고 중량을 범위내에서 찾고 가능한 경로를 걷는다.
'''

while left <= right:
	mid = (left + right) // 2
	vist = [0] * (V + 1)
	vist[f1] = 1
	if dfs(f1, f2, mid):
		left = mid + 1
		ans = max(ans, mid)
	else:
		right = mid - 1
print(ans)
