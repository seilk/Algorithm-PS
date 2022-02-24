import sys

input = sys.stdin.readline


def solution(info, edges):
  global cursheep
  N = len(info)
  tree = [[-1, -1] for i in range(N)]
  for i in range(N):
    if info[i] == 0:
      info[i] = -1  # 양을 -1로 바꿔줌
  for i in range(N - 1):
    parent, child = edges[i]
    if tree[parent][0] == -1:
      tree[parent][0] = child
    elif tree[parent][1] == -1:
      tree[parent][1] = child
  cursheep = 1
  find(0, tree, info, 1)
  return cursheep


def find(node, tree, info, tot):
  global cursheep
  left = tree[node][0]  # 왼쪽 노드
  right = tree[node][1]  # 오른쪽 노드
  if left > 0:
    if info[left] > 0:  # 늑대일 때
      if tot + info[left] <= 0:  # 늑대 >= 양
        return
      else :
        find(left, tree, info, tot + 1)
    else:  # 양일때
      cursheep += 1
      find(left, tree, info, tot - 1)

  if right > 0:
    if info[right] > 0:  # 늑대일 때
      if tot + right > 0:  # 늑대 < 양
        return
      else:
        find(right, tree, info, tot + 1)
    else:  # 양일때
      cursheep += 1
      find(right, tree, info, tot - 1)

solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])