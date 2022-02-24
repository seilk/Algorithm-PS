# ----------Title
# 최솟값과 최댓값
# Gold I
# https://www.acmicpc.net/problem/2357

# ----------Tip
# 세그먼트 트리

# ----------URLs


# ----------Code with Detail
import sys
from math import ceil, log2
sys.setrecursionlimit(10 ** 4)

def makesegtree_min(curnode, start, end):
  if start == end:
    segtree_min[curnode] = arr[start]
    return segtree_min[curnode]
  mid = (start + end) // 2
  left_result = makesegtree_min(curnode * 2, start, mid)
  right_result = makesegtree_min(curnode * 2 + 1, mid + 1, end)
  segtree_min[curnode] = min(left_result, right_result)
  return segtree_min[curnode]


def makesegtree_max(curnode, start, end):
  if start == end:
    segtree_max[curnode] = arr[start]
    return segtree_max[curnode]
  mid = (start + end) // 2
  left_result = makesegtree_max(curnode * 2, start, mid)
  right_result = makesegtree_max(curnode * 2 + 1, mid + 1, end)
  segtree_max[curnode] = max(left_result, right_result)
  return segtree_max[curnode]


def findsegmin(curnode, nodestart, nodeend, start, end):
  if end < nodestart or nodeend < start:
    return INF
  if start <= nodestart and nodeend <= end:
    return segtree_min[curnode]
  mid = (nodestart + nodeend) // 2
  left_min = findsegmin(curnode * 2, nodestart, mid, start, end)
  right_min = findsegmin(curnode * 2 + 1, mid + 1, nodeend, start, end)
  return min(left_min, right_min)


def findsegmax(curnode, nodestart, nodeend, start, end):
  if end < nodestart or nodeend < start:
    return -1
  if start <= nodestart and nodeend <= end:
    return segtree_max[curnode]
  mid = (nodestart + nodeend) // 2
  left_max = findsegmax(curnode * 2, nodestart, mid, start, end)
  right_max = findsegmax(curnode * 2 + 1, mid + 1, nodeend, start, end)
  return max(left_max, right_max)

if __name__ == "__main__":
  input = sys.stdin.readline
  INF = 1_000_000_000
  N, M = map(int, input().split())
  arr = [int(input()) for i in range(N)]
  segheight = ceil(log2(N))
  segsize = 1 << (segheight + 1) # len(arr) * 4

  segtree_min = [-1 for i in range(segsize)]
  segtree_max = [-1 for i in range(segsize)]
  makesegtree_min(1, 0, N - 1)
  makesegtree_max(1, 0, N - 1)

  for i in range(M):
    x0, x1 = map(int, input().split())
    ans_min = findsegmin(1, 0, N - 1, x0 - 1, x1 - 1)
    ans_max = findsegmax(1, 0, N - 1, x0 - 1, x1 - 1)
    print(ans_min, ans_max)