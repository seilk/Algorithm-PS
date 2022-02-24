# ----------Title
# 이진 검색 트리
# Silver I
# https://www.acmicpc.net/problem/5639

# ----------Tip
# Tree
# 트리 순회로 트리 재구성
# PreOrder로 Binary Search Tree 트리 재구성
# 트리 재구성 : 시간초과
# 전위순회에서 바로 후위순회로 바꾸는 방법 공부하기

# ----------URLs
# https://www.acmicpc.net/problem/1539

# ----------Code with Detail
from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)


def insert(parent, val):  # 트리의 전위순회로 트리 재구성 #시간초과
  if parent > val:
    if tree[parent][0] == -1:
      tree[parent][0] = val
    else:
      insert(tree[parent][0], val)
  else:
    if tree[parent][1] == -1:
      tree[parent][1] = val
    else:
      insert(tree[parent][1], val)


def postorder(root, left, right):

  if tree[root][0] != -1:
    postorder(left, tree[left][0], tree[left][1])

  if tree[root][1] != -1:
    postorder(right, tree[right][0], tree[right][1])

  print(root)


if __name__ == "__main__":
  input = sys.stdin.readline

  # preorder 작성
  preorder = []
  while 1:
    try:
      preorder.append(int(input().rstrip()))
    except:
      break
  root = preorder[0]

  # tree 초기화
  tree = dict()
  for i in range(len(preorder)):
    node = preorder[i]
    tree[node] = [-1, -1]

  # tree 작성
  for i in range(1, len(preorder)):
    insert(root, preorder[i])

  # postorder 작성
  postorder(root, tree[root][0], tree[root][1])


enumerate()
