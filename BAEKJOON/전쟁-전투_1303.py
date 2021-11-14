import sys
from collections import defaultdict, deque
def input(): return sys.stdin.readline().rstrip()


colsize, rowsize = map(int, input().split())
field = [list(input()) for i in range(rowsize)]
#
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0] * colsize for i in range(rowsize)]
queue = deque([])
res = [0, 0]
# 분할 BFS
# 모든 좌표를 탐색하면서 DFS알고리즘 적용
# BFS memoization에서 for문 안에서만 visited 조건 적용해야함
for i in range(rowsize):
    for j in range(colsize):
        if not visited[i][j]:
            queue.append([i, j])
            cnt = 1
            while queue:
                y, x = queue.popleft()
                code = field[y][x]
                visited[y][x] = 1
                for t in range(4):
                    new_y = y + dy[t]
                    new_x = x + dx[t]
                    if 0 <= new_y < rowsize and 0 <= new_x < colsize and not visited[new_y][new_x]:
                        if field[new_y][new_x] == code:
                            cnt += 1
                            visited[new_y][new_x] = 1
                            queue.append([new_y, new_x])
            if code == "W":
                res[0] += cnt ** 2
            else:
                res[1] += cnt ** 2

print(*res)
# w, u, flag_W, flag_B = 0, 0, True, True
# for y in range(rowsize):
#     for x in range(colsize):
#         code = field[y][x]
#         if not visited[y][x]:
#             visited[y][x] = 1
#             if code == "W":
#                 groups_W[u] += 1
#                 for i in range(4):
#                     new_x, new_y = x + dx[i], y + dy[i]
#                     if 0 <= new_x < colsize and 0 <= new_y < rowsize:
#                         if not visited[new_y][new_x] and field[new_y][new_x] == "W":
#                             visited[new_y][new_x] = 1
#                             groups_W[u] += 1
#                             flag = False
#                         elif i == 3 and flag_W:
#                             u += 1
#                             flag_W = True
#             if code == "B":
#                 groups_B[w] += 1
#                 for i in range(4):
#                     new_x, new_y = x + dx[i], y + dy[i]
#                     if 0 <= new_x < colsize and 0 <= new_y < rowsize:
#                         new_x, new_y = x + dx[i], y + dy[i]
#                         if not visited[new_y][new_x] and field[new_y][new_x] == "B":
#                             groups_B[w] += 1
#                             visited[new_y][new_x] = 1
#                         elif i == 3 and flag_B:
#                             w += 1
#                             flag_B = True
# power_B = sum([i**2 for i in list(groups_B.values())])
# power_W = sum([i ** 2 for i in list(groups_W.values())])


# while queue_W:
#     coord = queue_W.popleft()
#     if queue_W[coord[1]][coord[0]] == "W":
#         cnt_W += 1
#     y, x = coord[0], coord[1]
#     for i in range(4):
#         new_x , new_y = x + dx[i], y + dy[i]
#         if 0 <= new_x < colsize and 0 <= new_y < rowsize and not visited[new_y][new_x]:
#             if field[new_y][new_x] == "W":
#                 queue_W.append([new_y, new_x])
#                 visited[new_y][new_x] = 1
#                 cnt_W += 1
# #
# visited = [[0] * colsize for i in range(rowsize)]
# while queue_B:
#     coord = queue_B.popleft()
#     if queue_W[coord[1]][coord[0]] == "B":
#         cnt_B += 1
#     y, x = coord[0], coord[1]
#     for i in range(4):
#         new_x , new_y = x + dx[i], y + dy[i]
#         if 0 <= new_x < colsize and 0 <= new_y < rowsize and not visited[new_y][new_x]:
#             if field[new_y][new_x] == "B":
#                 queue_B.append([new_y, new_x])
#                 visited[new_y][new_x] = 1
#                 cnt_B += 1
