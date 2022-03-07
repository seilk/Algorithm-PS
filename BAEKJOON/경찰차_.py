import sys

sys.setrecursionlimit(10 ** 5)
In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


def calDist(x1, x2, y1, y2):
	return abs(x2 - x1) + abs(y2 - y1)


def rec(cap1, cap2, totDist, cap1pos, cap2pos):
	if cap1 == W or cap2 == W:
		return 0
	if totDist[cap1][cap2] != -1:
		return totDist[cap1][cap2]
	
	nextInc = max(cap1, cap2) + 1  # 다음 사건의 번호
	cap1Dist = calDist(cap1pos[0], inc[nextInc][0], cap1pos[1], inc[nextInc][1])  # cap1이 다음 사건을 처리할 때 거리
	cap2Dist = calDist(cap2pos[0], inc[nextInc][0], cap2pos[1], inc[nextInc][1])  # cap2이 다음 사건을 처리할 때 거리
	
	cap1NewDist = cap1Dist + rec(nextInc, cap2, totDist, inc[nextInc], cap2pos)  # cap1이 다음 사건처리 하는 경우
	cap2NewDist = cap2Dist + rec(cap1, nextInc, totDist, cap1pos, inc[nextInc])  # cap2가 다음 사건 처리 하는 경우
	
	if cap1NewDist < cap2NewDist:
		policeNum[cap1][cap2] = 1
		totDist[cap1][cap2] = cap1NewDist
	else:
		policeNum[cap1][cap2] = 2
		totDist[cap1][cap2] = cap2NewDist
	
	return totDist[cap1][cap2]


N = int(In())
W = int(In())
cap1 = (1, 1)
cap2 = (N, N)
totDist = [[-1] * (W + 1) for i in range(W + 1)] # 사건의 개수를 기준으로 배열 크기 잡아야함
inc = [(0, 0)] + [tuple(MIS()) for i in range(W)]
policeNum = [[0] * (W + 1) for i in range(W + 1)] # 사건의 개수를 기준으로 배열 크기 잡아야함
rec(0, 0, totDist, (1, 1), (N, N))
print(totDist[0][0])

x = 0
y = 0
for w in range(0, W):
	print(policeNum[x][y])
	if policeNum[x][y] == 1:
		x = w + 1
	else:
		y = w + 1
