import sys
sys.setrecursionlimit(10**6)
In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def init():
	N = int(In())
	pep = [-1] + [*MIS()]
	tree = [[] for i in range(N + 1)]
	for _ in range(N - 1):
		u, v = MIS()
		tree[u].append(v)
		tree[v].append(u)
	dp = [[-1, -1] for i in range(N + 1)]
	return N, pep, tree, dp


def rec(cur, pre, my):
	if dp[cur][my] != -1:
		return dp[cur][my]
	
	dp[cur][True], dp[cur][False] = pep[cur], 0
	for nxt in tree[cur]:
		if nxt == pre: continue
		# 현재 마을이 우수 마을일 때 -> 자식 마을은 일반 마을.
		dp[cur][True] += rec(nxt, cur, False)
		# 현재 마을이 일반 마을일 때 -> 자식 마을은 일반 or 우수 마을 중에서 인구 수 더 큰 마을
		dp[cur][False] += max(rec(nxt, cur, True), rec(nxt, cur, False))
	
	return dp[cur][my]
	
N, pep, tree, dp = init()
print(max(rec(1, 0, False), rec(1, 0, True)))

