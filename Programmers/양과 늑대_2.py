from collections import deque


def solution(info, edges):
  global MAX
  N = len(info)
  tree = [0] * N
  sheepnode = []
  for i in range(N):
    if info[i] == 0:
      sheepnode.append(i)

  for i in range(N - 1):
    parent, child = edges[i]
    tree[child] = parent

  sheepinfo = dict()
  for i in range(len(sheepnode)):
    sheepinfo[sheepnode[i]] = findwolf(sheepnode[i], set(), tree, info)
  sheeplst = deque(sorted(list(sheepinfo.items()), key=lambda x: len(x[1])))
  SUM_SHEEPS = 0
  while sheeplst:
    idx, w = sheeplst.popleft()
    if not w:
      SUM_SHEEPS += 1
      continue
    else:
      sheeplst.appendleft((idx, w))
      break
  visited = [0] * len(sheeplst)
  MAX = SUM_SHEEPS
  DFS(sheeplst, SUM_SHEEPS, visited, len(sheeplst), set())
  return MAX


def DFS(sheeplst, SUM_SHEEPS, visited, N, WOLVES):
  global MAX
  if MAX < SUM_SHEEPS:
    MAX = SUM_SHEEPS
  for i in range(N):
    if not visited[i]:
      if SUM_SHEEPS > len(WOLVES | sheeplst[i][1]):
        visited[i] = 1
        DFS(sheeplst, SUM_SHEEPS + 1, visited, N, WOLVES|sheeplst[i][1])
        visited[i] = 0


def findwolf(node, wolf, tree, info):
  if node == 0:
    return wolf
  if info[node] == 1:
    return findwolf(tree[node], wolf | {node}, tree, info)
  return findwolf(tree[node], wolf, tree, info)


# solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#          [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])
