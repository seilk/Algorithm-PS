import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

T = int(In())
for t in range(T):
	stk = 0
	ans = 0
	quiz = deque(list(In()))
	while quiz:
		a = quiz.popleft()
		if a == "O":
			stk += 1
		if a == "X":
			stk = 0
		ans += stk
	print(ans)