import sys
import copy
from collections import deque
def input(): return sys.stdin.readline().rstrip()


n = int(input())
areas = [list(map(int, input().split())) for i in range(n)]
maxx = max(map(max, areas))
minn = min(map(min, areas))
print(maxx, minn)
# drow = [1, -1, 0, 0]
# dcol = [0, 0, 1, -1]


def BFS(rrow, ccol, n, visited, rained):
    queue = deque([[rrow, ccol]])
    visited[rrow][ccol] = 1
    while queue:
        row, col = queue.popleft()
        for drow, dcol in (1, 0), (0, 1), (-1, 0), (0, -1):
            new_row = row + drow
            new_col = col + dcol
            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col]:
                if rained[new_row][new_col] != -1:
                    queue.append([new_row, new_col])
                    visited[new_row][new_col] = 1
    return


def rain(areas, h):
    for i in range(len(areas)):
        for j in range(len(areas)):
            if areas[i][j] <= h:
                areas[i][j] = -1
    return areas


ans = 1
for h in range(minn, maxx + 1):
    tmp = copy.deepcopy(areas)
    rained = rain(tmp, h)
    cnt = 0
    visited = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if rained[i][j] != -1 and not visited[i][j]:
                BFS(i, j, n, visited, rained)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
