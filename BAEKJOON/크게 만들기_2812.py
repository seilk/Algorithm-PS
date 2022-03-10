import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N, K = MIS()
num = deque(list(In()))
stk = []
chance = K
while num:
	n = num.popleft()
	if not stk:
		stk.append(n)
		continue
	while stk and chance > 0 and stk[-1] < n:
		stk.pop()
		chance -= 1
	stk.append(n)
print(*stk[:N-K],sep="")