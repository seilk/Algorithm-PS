import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


rowsize, colsize = map(int, input().split())
heights = list(map(int, input().split()))
world = [[0] * colsize for i in range(rowsize)]
for i in range(colsize):
    for j in range(rowsize - heights[i], rowsize):
        world[j][i] = 7
#
for i in range(rowsize):
    for j in range(colsize):
        if world[i][j] != 7:
            world[i][j] = 1

# for i in range(rowsize):
#     print(*world[i])


cnt = 0
for row in range(rowsize):
    idxs = deque([])  # []
    for col in range(colsize):
        if world[row][col] == 7:
            if len(idxs) == 1:
                idxs.append(col)
                pre = idxs.popleft()
                cnt += idxs[0] - pre - 1
                continue
            if len(idxs) == 0:
                idxs.append(col)
print(cnt)
# ceil_check = [0] * colsize
# ceil = [colsize - 1] * colsize
# for row in range(rowsize):
#     for col in range(colsize):
#         if world[row][col] == 7 and not ceil_check[col]:
#             ceil[col] = row
#             ceil_check[col] = True
#
# drow = [1, -1, 0, 0]
# dcol = [0, 0, 1, -1]
# visited = [[0] * colsize for i in range(rowsize)]


# def BFS(rrow, ccol, limit):
#     cnt = 1
#     queue = deque([[rrow, ccol]])
#     while queue:
#         row, col = queue.popleft()

#         for i in range(4):
#             new_row = row + drow[i]
#             new_col = col + dcol[i]
#             if limit <= new_row < rowsize and 0 <= new_col < colsize and not visited[new_row][new_col]:
#                 if world[new_row][new_col] == 0:
#                     visited[new_row][new_col] = 1
#                     world[new_row][new_col] = 1
#                     cnt += 1
#                     queue.append([new_row, new_col])
#     return cnt
# #


# ans = 0
# start = 1 if ceil[0][1] == 0 else 2
# for i in range(colsize - 1, start, -1):
#     for j in range(i - 1, -1, start):
#         if ceil[j] <= ceil[i]:
#             limit = ceil[j][0]
#             i = j
#             ans += BFS()

# if ceil[0][1] == 0 and len(ceil) > 1:
#     limit = min(ceil[0][0], ceil[1][0])
#     for row in range(limit, rowsize):
#         for col in range(ceil[step - 1][1] + 1, ceil[step][1]):
#             if world[row][col] == 0 and not visited[row][col]:
#                 visited[row][col] = 1
#                 world[row][col] = 1
#                 ans += BFS(row, col, limit)
# if ceil[-1][1] == 0 and len(ceil) > 1:
#     limit = min(ceil[-2][0], ceil[-1][0])
#     for row in range(limit, rowsize):
#         for col in range(ceil[step - 1][1] + 1, ceil[step][1]):
#             if world[row][col] == 0 and not visited[row][col]:
#                 visited[row][col] = 1
#                 world[row][col] = 1
#                 ans += BFS(row, col, limit)

# print(ans)
