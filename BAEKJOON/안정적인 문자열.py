import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def solve(target) :
	dq = deque(list(target))
	stack = []
	ans = 0
	while dq:
		cur = dq.popleft()
		if cur == "}":
			if not stack :
				ans += 1
				stack.append("{")
				continue
			stack.pop()

		else:
			stack.append(cur)
	return ans + len(stack) // 2

testCnt = 1
while 1 :
	target = In()
	if target[ 0 ] == "-" :
		break
	ans = solve(target)
	print(f"{testCnt}. {ans}")
	testCnt += 1
