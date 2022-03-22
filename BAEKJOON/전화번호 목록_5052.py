import sys
from collections import defaultdict

In = lambda: sys.stdin.readline().rstrip()


def init():
	n = int(In())
	arr = [In() for i in range(n)]
	arr.sort()
	dix = defaultdict(int)
	return arr, n, dix


def check() -> str:
	arr, n, dix = init()
	for num in arr:
		idx = 0
		s = ""
		for n in num:
			if dix[s]:
				return "NO"
			s += n
		if dix[s] : return "NO"
		dix[num] = True
	return "YES"


T = int(In())
for t in range(T):
	print(check())

# 1
# 3
# 1234
# 12
# 1