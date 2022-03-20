import sys
from collections import deque

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def init(N, M):
	mapp = [[*MIS()] for i in range(N)]
	order = [[*MIS()] for i in range(M)]
	dir = [(9,9), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
	cloud = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
	return mapp, order, dir, cloud


def moving(cloud, dir, dis):
	global mapp
	dx = dir[0] * dis
	dy = dir[1] * dis
	delCloud = [[0] * N for i in range(N)]
	increaseWater = deque([])
	while cloud:
		x, y = cloud.popleft()
		nx, ny = (x + dx) % N, (y + dy) % N
		increaseWater.append((nx, ny))
		delCloud[nx][ny] = 1
		mapp[nx][ny] += 1
	return delCloud, increaseWater


def copyWater(increaseWater):
	global mapp
	crossDir = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
	while increaseWater:
		x, y = increaseWater.popleft()
		cnt = 0
		for dx, dy in crossDir:
			nx, ny = x + dx, y + dy
			if 0 <= nx < N and 0 <= ny < N and mapp[nx][ny] > 0:
				cnt += 1
		mapp[x][y] += cnt


def makeCloud(delcloud):
	global mapp
	cloud = deque([])
	for i in range(N):
		for j in range(N):
			if mapp[i][j] >= 2 and delcloud[i][j] == 0:
				cloud.append((i, j))
				mapp[i][j] -= 2
	return cloud


def sumWater():
	global mapp
	ans = 0
	for i in range(N):
		for j in range(N):
			ans += mapp[i][j]
	return ans


N, M = MIS()
mapp, order, dir, cloud = init(N, M)
for d, s in order:
	curDir = dir[d]
	delCloud, increaseWater = moving(cloud, curDir, s)
	copyWater(increaseWater)
	cloud = makeCloud(delCloud)

print(sumWater())
