import sys


n = int(sys.stdin.readline().rstrip())

def floyd(n, matrix) : # 노드의 개수가 적을 때 가능한 모든 경로를 플로이드 와샬로 찾을 수 있음
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == 1 : continue
				if matrix[i][k] == 1 and matrix[k][j] == 1:
					matrix[i][j] = 1

	return matrix

matrix = [[*map(int, sys.stdin.readline().rstrip().split())] for i in range(n)]
ans = floyd(n, matrix)
for i in range(n):
	print(*ans[i])