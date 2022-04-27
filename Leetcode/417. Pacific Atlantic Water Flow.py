from collections import deque
from typing import List

class Solution :

	def bfs(self, zone, rowsize, colsize, heights) :
		dq = deque(zone)
		vist = [[0]*colsize for i in range(rowsize)]
		while dq :
			r, c = dq.popleft()
			vist[r][c] = 1
			val = heights[r][c]
			for nr, nc in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)] :
				if nr < 0 or nr >= rowsize or nc < 0 or nc >= colsize : continue
				if vist[nr][nc] == 1 : continue
				if heights[nr][nc] < val : continue
				vist[nr][nc] = 1
				dq.append((nr, nc))

		return vist

	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]] :
		rowsize = len(heights)
		colsize = len(heights[0])

		pacificZone = []
		atlanticZone = []
		for i in range(rowsize) :
			for j in range(colsize) :
				if i == 0 or j == 0 :
					pacificZone.append([i, j])
				if i == rowsize-1 or j == colsize-1 :
					atlanticZone.append([i, j])
		print(pacificZone)
		print(atlanticZone)
		vistPacific = self.bfs(pacificZone, rowsize, colsize, heights)
		vistAtlantic = self.bfs(atlanticZone, rowsize, colsize, heights)

		ans = []
		for i in range(rowsize) :
			for j in range(colsize) :
				if vistPacific[i][j] == 1 and vistAtlantic[i][j] == 1 :
					ans.append([i, j])

		return ans
