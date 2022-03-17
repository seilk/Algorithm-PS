import sys
from math import log2
sys.setrecursionlimit(10**5)
In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())

# https://alphatechnic.tistory.com/23 와 같은 실수를 함 (sparseTable 채우는 부분)

def init():
	N = int(In())
	tree = [[] for i in range(N + 1)]
	for n in range(N - 1):
		u, v = MIS()
		tree[u].append(v)
		tree[v].append(u)
	depth = [0] * (N + 1)
	MAX = int(log2(N)) + 1
	dp = [[0] * (MAX + 1) for i in range(N + 1)]
	M = int(In())
	return N, tree, depth, dp, M, MAX


def dfs(cur, pre, d):
	for nxt in tree[cur]:
		if nxt == pre: continue
		depth[nxt] = d + 1
		dp[nxt][0] = cur
		dfs(nxt, cur, d + 1)


def sparseTable():
	for j in range(1, MAX + 1):
		for i in range(1, N + 1):
			dp[i][j] = dp[dp[i][j - 1]][j - 1]


def findDepthDiff(u, v):
	return (depth[u] - depth[v], v, u) if depth[u] > depth[v] \
		else (depth[v] - depth[u], u, v)


def moving(depthDiff, mx):  # 깊이가 더 깊은 노드를 대상으로 깊이를 맞춰주는 작업
	j = 0
	jj = 1 << j
	while jj <= depthDiff:
		if depthDiff & jj:
			mx = dp[mx][j]
		j += 1
		jj = jj<<1
	'''
	diff = 8, 1000(2)
	j = 0, jj = 1
	j = 1, jj = 2
	j = 2, jj = 4
	j = 3, jj = 8 -> mx = dp[mx][3]
	'''
	return mx


def movingWith(mn, mx):  # 깊이는 같고 노드가 다를 경우 동시에 높이를 조절하면서 LCA 탐색
	for j in range(MAX-1, -1, -1):
		if dp[mx][j] == dp[mn][j]: continue
		if dp[mx][j] != 0 and dp[mx][j] != dp[mn][j]:
			mx = dp[mx][j]
			mn = dp[mn][j]
	ans = dp[mx][0]
	return ans


N, tree, depth, dp, M, MAX = init()
dfs(1, 0, 0)
sparseTable()

for m in range(M):
	u, v = MIS()
	depthDiff, mn, mx = findDepthDiff(u, v)
	mx = moving(depthDiff, mx)
	ans = mx
	if mn != mx:
		ans = movingWith(mn, mx)
	print(ans)