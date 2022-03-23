import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()

wordA = In()
wordB = In()
dqA = deque(list(wordA))
point = 0
lenB = len(wordB)
stack = []
while dqA:
	chr = dqA.popleft()
	if chr == wordB[point] and point == lenB - 1:
		for _ in range(lenB - 1):
			stack.pop()
		point = stack[-1][1] if stack else 0
		continue

	if chr == wordB[point]:
		stack.append((chr, point + 1))
		point += 1
	else:
		if chr == wordB[0]:
			stack.append((chr, 1))
			point = 1
		else:
			stack.append((chr, 0))
			point = 0
print(*[i[0] for i in stack] if len(stack) > 0 else "FRULA", sep = "")