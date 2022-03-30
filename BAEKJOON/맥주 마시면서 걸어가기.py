import sys
from collections import deque
from math import ceil

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def bfs(start, end, n, coord) :
	dq = deque([ start+[ 20 ] ]) # 좌표 + 맥주 개수
	vist = [ 0 ]*(n+2) # 각 좌표들의 방문 여부
	vist[ 0 ] = 1 # 시작점 방문 체크
	while dq :
		cx, cy, beer = dq.popleft()
		if cx == end[0] and cy == end[1]: # 도착점 일때 return "happy"
			return "happy"
		for i in range(n+2) :
			if vist[ i ] == 1 : continue # 이미 방문한 지점 재방문 X
			nx, ny = coord[ i ][ 0 ], coord[ i ][ 1 ] # 편의점 or 도착점의 x좌표, y좌표
			dist = abs(cx-nx)+abs(cy-ny) # manhattan dist
			if ceil(dist/50) > beer : continue # [1개/50m]이라서 51m 갈때는 2개 마셔야함, ceil 함수 사용
			vist[i] = 1
			nxtBeer = 20 if 1<=i<=n else beer - ceil(dist/50) # 편의점에 도착한다면 맥주 20개 소지 가능
			dq.append([nx, ny, nxtBeer])
	return "sad"

t = int(In())
for _ in range(t):
	n = int(In())
	coord = [ ]
	for i in range(n+2) :
		coord.append([ *MIS() ])

	print(bfs(coord[0], coord[-1], n, coord))

'''
1
2
0 0
500 0
1050 0
2050 0

1
2
0 0
1000 5
2000 10
3000 15
sad
'''