import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

N = int(In())
crane = [*MIS()]
M = int(In())
box = [*MIS()]
crane.sort(reverse=True)
box.sort(reverse=True)
if box[0] > crane[0]:
	print(-1)
else:
	cnt = 0
	time = 0
	while cnt < M:
		for c in range(N):
			for b in box:
				if crane[c] >= b:
					box.remove(b)
					cnt += 1
					break
		time += 1
	print(time)
# 3
# 1 1 1
# 5
# 1 1 1 1 10

# 2
# 8 8
# 3
# 9 9 9

# 3
# 10 10 1
# 6
# 10 10 1 10 10 1
