import sys
from collections import deque

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def findLeft(h):
	stack = []
	dq = deque(h)
	left = [0] * ll
	while dq:
		cur, idx = dq.popleft()
		while stack and stack[-1][0] >= cur:
			stack.pop()
		if not stack:
			left[idx] = -1
			stack.append((cur, idx))
			continue
		left[idx] = stack[-1][1]
		stack.append((cur, idx))
	return left


def findRight(h):
	stack = []
	dq = deque(h[::-1])
	right = [0] * ll
	while dq:
		cur, idx = dq.popleft()
		while stack and stack[-1][0] >= cur:
			stack.pop()
		if not stack:
			right[idx] = ll
			stack.append((cur, idx))
			continue
		right[idx] = stack[-1][1]
		stack.append((cur, idx))
	return right


while 1:
	ll, *h = MIS()
	if ll == 0: break
	hh = [(val, i) for i, val in enumerate(h)]
	left = findLeft(hh)
	right = findRight(hh)
	mxx = 0
	for i in range(ll):
		mxx = max(mxx, hh[i][0] * (right[i] - left[i] - 1))
	print(mxx)
