import sys
from collections import defaultdict

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())

T = int(In())
for t in range(T):
	word = In()
	dix = defaultdict(int)
	pos = defaultdict(list)
	for c in range(len(word)):
		dix[word[c]] += 1
		pos[word[c]].append(c)

	K = int(In())
	check = []
	for key, val in dix.items():
		if val >= K:
			check.append(key)

	if len(check) == 0:
		print(-1)
		continue

	ans1 = 10000
	ans2 = 0
	for al in check:  # 26
		ans1 = min(ans1, min(pos[al][i + K - 1] - pos[al][i] + 1 for i in range(len(pos[al]) - K + 1)))
		ans2 = max(ans2, max(pos[al][-i] - pos[al][-(i + K - 1)] + 1 for i in range(1, len(pos[al]) - K + 1 + 1)))
	print(ans1, ans2)
