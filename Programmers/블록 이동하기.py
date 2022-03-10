from collections import deque, defaultdict


def swap(a, b):
	return b, a


def BFS(start, N, board):
	dq = deque(start)
	move = [(1, 0, 1, 0), (-1, 0, -1, 0),  # 위, 아래 이동
					(0, 1, 0, 1), (0, -1, 0, -1)]
	
	rotate1Up = [(-1, 1, 0, 0), (0, 0, -1, -1)]
	rotate1Down = [(1, 1, 0, 0), (0, 0, 1, -1)]
	rotate2Right = [(1, 1, 0, 0), (0, 0, -1, 1)]
	rotate2Left = [(1, -1, 0, 0), (0, 0, -1, -1)]
	check = []
	
	for x1, y1, x2, y2, cnt in start:
		check.append({(x1,y1),(x2,y2)})
	
	while dq:
		x1, y1, x2, y2, cnt = dq.popleft()
		if y1 == y2 and x1 > x2:
			x1, x2 = swap(x1, x2)
		if x1 == x2 and y1 > y2:
			y1, y2 = swap(y1, y2)
		
		if (x1, y1) == (N - 1, N - 1) or (x2, y2) == (N - 1, N - 1):
			return cnt
		
		res = []  # 가능한 좌표 모음
		for d1, d2, d3, d4 in move:
			nx1, ny1, nx2, ny2 = x1 + d1, y1 + d2, x2 + d3, y2 + d4
			# 범위 조건
			if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
				if board[nx1][ny1] == 1 or board[nx2][ny2] == 1: continue
				res.append((nx1, ny1, nx2, ny2, cnt))
		
		if x1 == x2:  # 가로 회전
			if 0 <= x1 - 1 < N and 0 <= x2 - 1 < N:
				if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
					for d1, d2, d3, d4 in rotate1Up:
						nx1, ny1, nx2, ny2 = x1 + d1, y1 + d2, x2 + d3, y2 + d4
						if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
							res.append((nx1, ny1, nx2, ny2, cnt))
			
			if 0 <= x1 + 1 < N and 0 <= x2 + 1 < N:
				if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
					for d1, d2, d3, d4 in rotate1Down:
						nx1, ny1, nx2, ny2 = x1 + d1, y1 + d2, x2 + d3, y2 + d4
						if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
							res.append((nx1, ny1, nx2, ny2, cnt))
		
		if y1 == y2:  # 세로 회전
			if 0 <= y1 + 1 < N and 0 <= y2 + 1 < N:
				if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
					for d1, d2, d3, d4 in rotate2Right:
						nx1, ny1, nx2, ny2 = x1 + d1, y1 + d2, x2 + d3, y2 + d4
						if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
							res.append((nx1, ny1, nx2, ny2, cnt))
			
			if 0 <= y1 - 1 < N and 0 <= y2 - 1 < N:
				if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
					for d1, d2, d3, d4 in rotate2Left:
						nx1, ny1, nx2, ny2 = x1 + d1, y1 + d2, x2 + d3, y2 + d4
						if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
							res.append((nx1, ny1, nx2, ny2, cnt))
		
		for nx1, ny1, nx2, ny2, cnt in res:
			cur = {(nx1, ny1), (nx2, ny2)}
			if cur in check: continue
			check.append(cur)
			dq.append((nx1, ny1, nx2, ny2, cnt + 1))


def solution(board):
	N = len(board)
	start = [(0, 0, 0, 1, 0)]
	return BFS(start, N, board)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0],
								[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1],
								[0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))

print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0],
								[0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0],
								[0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))

print(solution(
	[[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
