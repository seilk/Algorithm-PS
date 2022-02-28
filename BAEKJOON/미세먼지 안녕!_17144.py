import sys
from copy import deepcopy

from collections import deque

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def findAirCleanPos():
	for i in range(0, R):
		if ground[i][0] == -1:
			break
	return i, i + 1


def findDustPos(ground):
	dustDeque = deque([])
	for i in range(R):
		for j in range(C):
			if ground[i][j] > 0:
				dustDeque.append((i, j))
	return dustDeque


def dustDiffusion(dustDeque, topCleanPos, botCleanPos, ground):
	newGround = [[0] * C for i in range(R)]
	newGround[topCleanPos][0] = -1
	newGround[botCleanPos][0] = -1
	
	while dustDeque:
		x, y = dustDeque.popleft()
		gauge = ground[x][y] // 5
		cnt = 0
		for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
			if 0 <= nx < R and 0 <= ny < C and newGround[nx][ny] != -1:
				cnt += 1
				newGround[nx][ny] += gauge
		newGround[x][y] += ground[x][y] - (gauge * cnt)
	
	return newGround


def windTop(top, newGround):
	topDownRow = newGround[top][1:]
	topRightCol = [newGround[i][C - 1] for i in range(top - 1, -1, -1)]
	topUpRow = newGround[0][:C - 1][::-1]
	topLeftCol = [newGround[i][0] for i in range(1, top)]
	newTop = deque(topDownRow + topRightCol + topUpRow + topLeftCol)
	newTop.appendleft(0)
	newTop.pop()
	for j in range(1, C):
		newGround[top][j] = newTop.popleft()
	for i in range(top - 1, -1, -1):
		newGround[i][C - 1] = newTop.popleft()
	for j in range(C - 2, -1, -1):
		newGround[0][j] = newTop.popleft()
	for i in range(1, top):
		newGround[i][0] = newTop.popleft()
	return newGround


def windBot(bot, newGround):
	botUpRow = newGround[bot][1:]
	botRightCol = [newGround[i][C - 1] for i in range(bot + 1, R)]
	botDownRow = newGround[R - 1][:C - 1][::-1]
	botLeftCol = [newGround[i][0] for i in range(R - 2, bot, -1)]
	newBot = deque(botUpRow + botRightCol + botDownRow + botLeftCol)
	newBot.appendleft(0)
	newBot.pop()
	for j in range(1, C):
		newGround[bot][j] = newBot.popleft()
	for i in range(bot + 1, R):
		newGround[i][C - 1] = newBot.popleft()
	for j in range(C - 2, -1, -1):
		newGround[R - 1][j] = newBot.popleft()
	for i in range(R - 2, bot, -1):
		newGround[i][0] = newBot.popleft()
	return newGround


def totDust(ground):
	return sum([sum(ground[i]) for i in range(R)]) + 2


R, C, T = MIS()
ground = [[*MIS()] for i in range(R)]
topCleanPos, botCleanPos = findAirCleanPos()

for t in range(T):
	dustDeque = findDustPos(ground)
	newGround = dustDiffusion(dustDeque, topCleanPos, botCleanPos, ground)
	newGround = windTop(topCleanPos, newGround)
	newGround = windBot(botCleanPos, newGround)
	ground = list(newGround)

print(totDust(ground))

# 6 3 1
# -1 -1 -1
# 0 30 7
# -1 10 0
# -1 0 20
# -1 -1 -1
# -1 -1 -1

# 8 8 2
# 3 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0