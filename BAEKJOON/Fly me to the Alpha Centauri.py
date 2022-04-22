import sys
from math import sqrt, ceil

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

t = int(In())
for _ in range(t) :
	x, y = MIS()
	diff = y-x
	r = int(sqrt(diff))
	ans = -1
	left = r
	right = r+1
	if r*r == diff :
		ans = 2*r-1
	elif diff >= ceil((left*left+right*right)/2) :
		ans = 2*r+1
	else :
		ans = 2*r

	print(ans)
