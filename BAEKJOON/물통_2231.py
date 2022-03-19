import sys
from collections import deque

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def bfs(start, limit):
	limitA = limit[0]
	limitB = limit[1]
	limitC = limit[2]
	dq = deque([start])
	ans = set()
	while dq:
		a, b, c = dq.popleft()
		if (a, b, c) in comb: continue
		comb.add((a, b, c))
		if a == 0:
			ans.add(c)
		if a > 0:
			if a + c >= limitC:
				dq.append((a + c - limitC, b, limitC))
			else:
				dq.append((0, b, c + a))
			if a + b >= limitB:
				dq.append((a + b - limitB, limitB, c))
			else:
				dq.append((0, b + a, c))
		
		if b > 0:
			if b + a >= limitA:
				dq.append((limitA, a + b - limitA, c))
			else:
				dq.append((a + b, 0, c))
			if b + c >= limitC:
				dq.append((a, b + c - limitC, limitC))
			else:
				dq.append((a, 0, b + c))
		
		if c > 0:
			if c + a >= limitA:
				dq.append((limitA, b, c + a - limitA))
			else:
				dq.append((a + c, b, 0))
			if c + b >= limitB:
				dq.append((a, limitB, c + b - limitB))
			else:
				dq.append((a, b + c, 0))
	
	return sorted(list(ans))


limit = [*MIS()]
comb = set()

print(*bfs((0, 0, limit[-1]), limit))
