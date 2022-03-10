import sys
from collections import deque

def back(x):
	return x-1

def forward(x):
	return x+1

def teleport(x):
	return x * 2

def cmd(idx, x):
	if idx == 0:
		return back(x)
	if idx == 1:
		return forward(x)
	else:
		return teleport(x)
	
def BFS(cur, B):
	dq = deque([(cur, 0)])
	vist = [0] * 1_000_001
	vist[cur] = 1
	while dq:
		x, t = dq.popleft()
		if x == B:
			return t
		for i in range(3):
			n = cmd(i, x)
			if n < 0 or n > 1_000_000 : continue
			if not vist[n]:
				vist[n] = 1
				dq.append((n, t+1))
	
A, B = map(int, sys.stdin.readline().split())
print(BFS(A, B))










