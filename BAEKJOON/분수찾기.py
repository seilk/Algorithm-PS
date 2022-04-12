import sys

In = lambda : sys.stdin.readline().rstrip()

n = int(In())

def findSum(n) :
	return n*(n+1)//2

for i in range(1, 5000) :
	if n <= findSum(i):
		break
if i & 1 == 0:
	bot = 1
	top = i
	diff = findSum(i) - n
	top -= diff
	bot += diff
	print(f"{top}/{bot}")
else:
	bot = i
	top = 1
	diff = findSum(i)-n
	top += diff
	bot -= diff
	print(f"{top}/{bot}")