import sys
import math
sys.setrecursionlimit(10**4)

def makeSegtree(curnode, start, end):
  if start == end:
    segtree[curnode] = arr[start]
    return segtree[curnode]
  mid = (start + end) // 2
  left = makeSegtree(curnode * 2, start, mid)
  right = makeSegtree(curnode * 2 + 1, mid + 1, end)
  segtree[curnode] = left + right
  return segtree[curnode]


def sumSegtree(curnode, nodestart, nodeend, start, end):
  if start <= nodestart and nodeend <= end:
    return segtree[curnode]
  if nodeend < start or end < nodestart:
    return 0
  mid = (nodestart + nodeend) // 2
  left = sumSegtree(curnode * 2, nodestart, mid, start, end)
  right = sumSegtree(curnode * 2 + 1, mid + 1, nodeend, start, end)
  return left + right


def valChangeSegtree(curnode, nodestart, nodeend, idx, diff):
  if idx < nodestart or nodeend < idx:
    return
  segtree[curnode] += diff
  if nodestart != nodeend:
    mid = (nodestart + nodeend) // 2
    left = valChangeSegtree(curnode * 2, nodestart, mid, idx, diff)
    right = valChangeSegtree(curnode * 2 + 1, mid + 1, nodeend, idx, diff)


def solve():
  makeSegtree(1, 0, N - 1)
  for i in range(Q):
    x0, x1, idx, to = map(int, input().split())
    if x0 > x1:
      tmp = x1
      x1 = x0
      x0 = tmp
    print(sumSegtree(1, 0, N - 1, x0 - 1, x1 - 1))
    diff = to - arr[idx - 1]
    arr[idx - 1] += diff
    valChangeSegtree(1, 0, N - 1, idx - 1, diff)

input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
segheight = int(math.ceil(math.log2(N)))
segsize = 1 << (segheight + 1)
segtree = [-1 for i in range(segsize)]
solve()