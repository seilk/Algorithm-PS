import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())


n = int(In())
brd = [[*MIS()] for i in range(n)]

dq = deque([(0, 0)])
vist = [[0]*n for i in range(n)]
ans = 0
while dq :
	y, x = dq.popleft()
	if y == n-1 and x == n-1 :
		ans += 1
		continue

	d = brd[y][x]
	for nx, ny in [(y+d, x), (y, x+d)] :
		if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
		if vist[ny][nx] == 1 : continue
		dq.append((ny, nx))
print(ans)