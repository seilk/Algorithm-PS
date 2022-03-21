import sys

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def fillBlock(N, mark: int, cnt):
	board = [[0] * N for i in range(N)]

	yy = 0
	while yy < N:
		y = yy
		x = 0
		while y >= 0:
			board[x][y] = mark
			x += 1
			y -= 1
			cnt -= 1
			if cnt == 0: return board
		yy += 1

	xx = 1
	while xx < N:
		x = xx
		y = N - 1
		while x < N:
			board[x][y] = mark
			x += 1
			y -= 1
			cnt -= 1
			if cnt == 0 : return board
		xx += 1
	return board


def fillOtherBlock(N, mark, cnt):
	global board
	yy = N - 1
	while yy >= 0:
		x = N - 1
		y = yy
		while y < N:
			for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
				if x + dx < 0 or x + dx >= N or y + dy < 0 or y + dy >= N: continue
				if board[x + dx][y + dy] == 1: return False
			board[x][y] = mark
			x -= 1
			y += 1
			cnt -= 1
			if cnt == 0: return board
		yy -= 1

	yy = N - 2
	while 0 <= yy:
		x = 0
		y = yy
		while y >= 0:
			for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
				if x + dx < 0 or x + dx >= N or y + dy < 0 or y + dy >= N: continue
				if cnt > 0 and board[x + dx][y + dy] == 1: return False
			board[x][y] = mark
			x += 1
			y -= 1
			cnt -= 1
			if cnt == 0 : return board
		yy -= 1
	return board


N = int(In())
c, e = MIS()
C = 1
E = 2
if N == 1:
	print(-1)
	sys.exit(0)

board = fillBlock(N, C, c)
if fillOtherBlock(N, E, e):
	print(1)
	for i in range(N):
		print(*board[i], sep="")
else:
	print(-1)
