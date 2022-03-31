import sys
from collections import deque

In = lambda:sys.stdin.readline().rstrip()
MIS = lambda:map(int,In().split())


def BFS(N,M,K,board,sx=0,sy=0):
	dq = deque([ (sx,sy,K) ])  # 현재까지 벽을 부순 개수
	vist = [ [ [ -1 ]*(K+1) for i in range(M) ] for j in range(N) ]
	for i in range(0,K + 1):
		vist[0][0][i] = 0
	dknight = [ (-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2) ]
	while dq:
		cx,cy,k = dq.popleft()

		if cx==N-1 and cy==M-1:
			return vist[ cx ][ cy ]
		if k > 0:
			for dx,dy in dknight:
				nx,ny = cx+dx,cy+dy
				if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
				if board[ nx ][ ny ]==1: continue
				if vist[ nx ][ ny ][ k-1 ] != -1: continue
				vist[ nx ][ ny ][ k-1 ] = vist[ cx ][ cy ][ k ]+1
				dq.append((nx,ny,k-1))
		for dx,dy in [ (0,-1),(0,1),(1,0),(-1,0) ]:
			nx,ny = cx+dx,cy+dy
			if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
			if board[ nx ][ ny ]==1: continue
			if vist[ nx ][ ny ][ k ] != -1 : continue
			vist[ nx ][ ny ][ k ] = vist[ cx ][ cy ][ k ]+1
			dq.append((nx,ny,k))
	return -1


if __name__=="__main__":
	K = int(In())
	M,N = MIS()
	board = [ [ *MIS() ] for i in range(N) ]
	ans = BFS(N,M,K,board)
	if ans == -1:
		print(-1)
	else:
		print(min(ans[i] for i in range(K + 1) if ans[i] > -1))


