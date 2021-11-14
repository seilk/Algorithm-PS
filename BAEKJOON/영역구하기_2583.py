from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


rowsize, colsize, k = map(int, input().split())
squares = [list(map(int, input().split())) for i in range(k)]
ground = [[0] * colsize for i in range(rowsize)]

for square in squares:
    for i in range(square[0], square[2]):
        for j in range(rowsize - square[3], rowsize - square[1]):
            ground[j][i] = -1

queue = deque([])
visited = [[0] * colsize for i in range(rowsize)]
drow = [0, 0, -1, 1]
dcol = [1, -1, 0, 0]


def BFS(rrow, ccol, visited, queue, ground, regions):
    queue.append([rrow, ccol])
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            new_row = row + drow[i]
            new_col = col + dcol[i]
            if 0 <= new_row < rowsize and 0 <= new_col < colsize and not visited[new_row][new_col]:
                if ground[new_row][new_col] == 0:
                    visited[new_row][new_col] = 1
                    queue.append([new_row, new_col])
                    regions += 1
    return regions


ans = []
for row in range(rowsize):
    for col in range(colsize):
        if ground[row][col] == 0 and not visited[row][col]:
            visited[row][col] = 1
            ans.append(BFS(row, col, visited, queue, ground, 1))
ans.sort()
print(len(ans))
print(*ans)
